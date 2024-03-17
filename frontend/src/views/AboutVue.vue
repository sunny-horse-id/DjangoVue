<script setup>

</script>

<template>
  <div style="position: fixed; top: 0; left: 0; width: 100%;">
    <el-scrollbar max-height="730px">
      <nav class="navbar navbar-expand-lg navbar-light bg-light" style="width: 100%">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>
              <div class="dropdown-menu">
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Something else here</a>
              </div>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li>
          </ul>
          <div style="width: 700px"></div>
          <form>
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">

          </form>
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </div>
      </nav>
      <div style="width: 100%; background-color: rgba(222,218,194,0.47)">
        <div style="margin: 0 auto; width: 60%; padding-top: 5px">
        </div>
        <div style="background-color: #f8f8f8; width: 61.6%; margin: 0 auto; border-radius: 20px 20px 0 0">
          <div style="height: 50px"></div>
          <div class="text-center"><h3>舞</h3></div>
          <div style="height: 20px"></div>
          <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-3">
              <img src="@/assets/images/about/logo.png" alt="">
            </div>
            <div class="col-md-6">
              <div style="height: 25px"></div>
              <p style="color: rgba(166,162,162,0.84)">
                欢迎来到我们的网站！我们致力于为您提供免费的舞蹈学习体验。
                通过先进的人工智能生成舞蹈，我们为您带来独特的学习方式。
                无论您是想学习跳舞还是寻找创作灵感，我们都为您提供了丰富的舞蹈视频资源。
                我们的愿景是成为教育力量薄弱地区孩子们的舞蹈老师，让更多人享受跳舞的乐趣，探索舞蹈的无限可能。
                让我们一起跳动起来，感受舞蹈的魅力！
              </p>
            </div>
            <div class="col-md-2"></div>
          </div>
        </div>
        <div
            style="width: 61.6%; margin: 0 auto; background: linear-gradient(to bottom, rgba(239,230,193,0.75), #f8f8f2); border-radius: 0 0 20px 20px">
          <div style="height: 50px"></div>
          <div class="text-center"><h3>团队理念</h3></div>
          <div style="height: 20px"></div>
          <div class="text-center" style="width: 10%; margin: 0 auto; background-color: #dfe3cd">
            <h5>使命</h5>
          </div>
          <div class="text-center">
            <h4>助力每一个渴望起舞的人</h4>
            <p style="color: rgba(166,162,162,0.84)">Help everyone who wants to dance</p>
          </div>
          <div style="height: 15px"></div>
          <div class="text-center" style="width: 10%; margin: 0 auto; background-color: #dfe3cd">
            <h5>价值观</h5>
          </div>
          <div style="height: 5px"></div>
          <div style="width: 90%; margin: 0 auto;">
            <el-row :gutter="20">
              <el-col :span="6">
                <div style="background-color: #e3e3df; border-radius: 15px">
                  <div style="height: 20px"></div>
                  <div style="margin: 0 auto; width: 20%">
                    <img src="@/assets/images/about/dang.png" alt="" style="width: 40px; height: 40px; ">
                  </div>
                  <div style="height: 10px;"></div>
                  <div class="text-center">
                    <h5>勇于担当</h5>
                    <p style="font-weight: lighter; font-size: smaller">
                      为全球教育资源匮乏地区的孩子们提供舞蹈学习机会，同时为跳舞者们提供创作灵感。
                      让舞蹈成为连接世界、表达个性和促进文化交流的力量。
                    </p>
                  </div>
                </div>
              </el-col>
              <el-col :span="6">
                <div style="background-color: #e3e3df; border-radius: 15px">
                  <div style="height: 20px"></div>
                  <div style="margin: 0 auto; width: 20%">
                    <img src="@/assets/images/about/time.png" alt="" style="width: 40px; height: 40px;">
                  </div>
                  <div style="height: 10px;"></div>
                  <div class="text-center">
                    <h5>与时俱进</h5>
                    <p style="font-weight: lighter; font-size: smaller">
                      致力于融合先进技术与舞蹈教育，通过使用DDPM等技术，您实现了音乐生成舞蹈的创新方法，为学习者提供了全新的学习体验。
                    </p>
                  </div>
                </div>
              </el-col>
              <el-col :span="6">
                <div style="background-color: #e3e3df; border-radius: 15px">
                  <div style="height: 20px"></div>
                  <div style="margin: 0 auto; width: 20%">
                    <img src="@/assets/images/about/heart.png" alt="" style="width: 40px; height: 40px;">
                  </div>
                  <div style="height: 10px;"></div>
                  <div class="text-center">
                    <h5>独具匠心</h5>
                    <p style="font-weight: lighter; font-size: smaller">
                      通过精心的布局和优雅的设计，不仅实现功能，更传达情感，吸引用户，成为技术与艺术的完美结合。
                    </p>
                  </div>
                  <div style="height: 6px"></div>
                </div>
              </el-col>
              <el-col :span="6">
                <div style="background-color: #e3e3df; border-radius: 15px">
                  <div style="height: 20px"></div>
                  <div style="margin: 0 auto; width: 20%">
                    <img src="@/assets/images/about/beyond.png" alt="" style="width: 40px; height: 40px;">
                  </div>
                  <div style="height: 10px;"></div>
                  <div class="text-center">
                    <h5>超越自我</h5>
                    <p style="font-weight: lighter; font-size: smaller">
                      创造出独特的用户体验,挑战技术边界，不断学习和创新，实现美学与功能的完美平衡，展现了独特的才华和创造力。
                    </p>
                  </div>
                  <div style="height: 6px"></div>
                </div>
              </el-col>
            </el-row>
          </div>
        </div>
      </div>
      <div style="height: 10px; background-color: rgba(222,218,194,0.47)"></div>
      <div class="container-fluid text-center"
           style="background-color: #313133; padding-top: 10px;">
        <div class="copyright">
          <p>
            <a href="javascript:;">关于我们</a>
            <a href="javascript:;">帮助中心</a>
            <a href="javascript:;">搜索推荐</a>
            <a href="javascript:;">友情链接</a>
          </p>
          <p>CopyRight © 舞</p>
        </div>
      </div>
    </el-scrollbar>
  </div>
</template>

<style scoped>
.copyright {
  height: 120px;
  padding-top: 40px;
  text-align: center;
  color: #999;
  font-size: 15px;

  p {
    line-height: 1;
    margin-bottom: 20px;
  }

  a {
    color: #999;
    line-height: 1;
    padding: 0 10px;
    border-right: 1px solid #999;

    &:last-child {
      border-right: none;
    }
  }
}
</style>