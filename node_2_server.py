import lib 




if __name__ == '__main__':
    port = 50052
    node_id = 3
    datapath = '/node3'


    lib.FileServer(port, node_id, datapath).start(50052)
