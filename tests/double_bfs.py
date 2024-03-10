''' nouvelle idee :double BFS
   def double_bfs(graph, src, dst):
      seen_src=set()
      seen_dst=set()
      queue_src=deque([src])
      pred_src={src: None} 
      queue_dst=deque([dst])
      pred_dst={dst: None}  
      
      i=0
      while queue_src and queue_dst:
          i=i+1
          noeud_cur_src=queue_src.popleft()
          noeud_cur_dst=queue_dst.popleft()
          print(noeud_cur_src)
          print(noeud_cur_dst)
          if noeud_cur_src in seen_dst:
            #Reconstruire le chemin à partir de noeud_cur_src
            Chemin = [noeud_cur_dst]
            while pred_dst[noeud_cur_dst] is not dst:
                noeud_cur_dst = pred_dst[noeud_cur_dst]
                Chemin.append(noeud_cur_dst)
                print(noeud_cur_src)
                print(noeud_cur_dst)
            Chemin.append(dst)
            Chemin.reverse()

            while pred_src[noeud_cur_src] is not src:
                noeud_cur_src = pred_src[noeud_cur_src]
                Chemin.append(noeud_cur_src)
            Chemin.append(src)
            Chemin.reverse()
            return Chemin

          if noeud_cur_dst in seen_src:
              Chemin = [noeud_cur_dst]
              while pred_dst[noeud_cur_dst] is not dst:
                noeud_cur_dst = pred_dst[noeud_cur_dst]
                Chemin.append(noeud_cur_dst)
                print(noeud_cur_src)
                print(noeud_cur_dst)
              Chemin.append(dst)

              while pred_src[noeud_cur_src] is not src:
                noeud_cur_src = pred_src[noeud_cur_src]
                Chemin.append(noeud_cur_src)
              Chemin.append(src)
              Chemin.reverse()
              return Chemin




          grille_init =Grid(len(src),len(src[0]),tuple_into_matrice(noeud_cur_src))
          voisins1=grille_init.adjacent_grids()    #voisins du noeud cur du  BFS 1
    

    
          for grille in voisins1:
            new=Graph.matrice_into_tuple(grille)
            if new not in seen_src:
              queue_src.append(new)
              pred_src[new]=noeud_cur_src
              seen_src.add(new)

          grille_init2 = Grid(len(src),len(src[0]),tuple_into_matrice(noeud_cur_dst))
          voisins2=grille_init2.adjacent_grids()   #voisins du noeud cur du  BFS 2
    
          for grille in voisins2:
              new=Graph.matrice_into_tuple(grille)
              if new not in seen_dst:
                  queue_dst.append(new)
                  pred_dst[new]=noeud_cur_dst
                  seen_dst.add(new)

      return None
'''
