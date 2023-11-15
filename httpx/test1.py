import wikipediaapi
import time
import sys
sys.setrecursionlimit(1500)


def bfs(pages_queue, stop_page, path: dict[str, str]) -> str:
    if len(pages_queue) == 0:
        raise Exception('queue is empty')

    current_page = pages_queue.pop(0)

    if current_page.title == stop_page.title:
        return stop_page.title

    try:
        all_subpages = current_page.links
        # print(f'Visited {current_page}')
    except Exception:
        all_subpages = {}

    if all_subpages.get(stop_page.title, None):
        path[stop_page.title] = current_page.title
        return stop_page.title

    for subpage in all_subpages.values():
        if subpage.title == current_page.title \
                or subpage in path.keys():
            continue
        pages_queue.append(subpage)
        path[subpage.title] = current_page.title

    return bfs(pages_queue, stop_page, path)


def create_path(start_page: str, page: str, path_dict: dict[str, str]) -> list[str]:
    path = []
    print()
    while path_dict[page] != start_page:
        path.append(page)
        page = path_dict[page]
        if page in path:
            break
    path.append(page)
    path.append(start_page)
    path.reverse()
    print(path)
    R = dict()
    for i, n in enumerate(path):
        R.setdefault(n, []).append(i)
    R = {n: rep for n, rep in R.items() if len(rep) > 1}

    print(path)
    if len(R) != 0:
        duplicate = ""
        for key in R:
            duplicate = key
        start = R[duplicate][0]
        end = R[duplicate][-1]
        path = path[:start] + path[end:]
            
    return path


def find_path(page_from, page_to):
    wiki_wiki = wikipediaapi.Wikipedia('CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)', "ru")
    nodes_dict = {}
    start_page = wiki_wiki.page(page_from)
    end_page = wiki_wiki.page(page_to)

    if not start_page.exists():
        return 'start page is not exists'
    if not end_page.exists():
        return 'end page is not exists'

    nodes_dict[start_page.title] = start_page.links
    queue = [start_page]
    end = bfs(queue, end_page, nodes_dict)
    path = create_path(start_page.title, end, nodes_dict)
    return f"Путь от {start_page.title} до {end_page.title} составляет {len(path) - 1}\n"\
           + " -> ".join(path)


def main():
    start_page = 'Философия'
    end_page = 'Машина'
    path = find_path(start_page, end_page)
    print(path)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Поиск занял %s seconds" % (time.time() - start_time))