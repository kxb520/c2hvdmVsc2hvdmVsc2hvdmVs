<div>
<a href="https://www.hscsec.cn">
    <img
      src="./img/favicon.ico"
      alt="shovel"
      height="64"
    />
</a>
  <h3>
    <b>
      SHOVEL
    </b>
  </h3>
  <a href="https://git.io/typing-svg"><img  src="https://readme-typing-svg.herokuapp.com?font=ZCOOL+KuaiLe&pause=1000&color=FFFFFF&width=435&lines=%E8%A7%A3%E6%94%BE%E5%8F%8C%E6%89%8B%EF%BC%8C%E4%B8%8D%E5%81%9A%E5%90%97%E5%96%BD" alt="Typing SVG" /></a>
  <p>

![Made with React Router](https://img.shields.io/badge/Made%20with-React%20Router-FF4B2B?style=for-the-badge&logo=react-router&logoColor=white)
![Made with Ant Design](https://img.shields.io/badge/Made%20with-Ant%20Design-0170FE?style=for-the-badge&logo=ant-design&logoColor=white)
![Made with MapLibre GL JS](https://img.shields.io/badge/Made%20with-MapLibre%20GL%20JS-1A73E8?style=for-the-badge&logo=mapbox&logoColor=white)
![Made with Hammer.js](https://img.shields.io/badge/Made%20with-Hammer.js-FCA121?style=for-the-badge&logo=javascript&logoColor=black)
![Powered by Nginx](https://img.shields.io/badge/Powered%20by-Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

  </p>

  <p>
    <sub>
       power ❤︎ by
      <a href="https://www.hscsec.cn">
        hscsec
      </a>
    </sub>
  </p>

  <br />

  <p>
    <img
      src="./img/task.jpg"
      alt="shovel"
      height="500"
    />
  </p>
</div>




### 🔍 重新定义企业资产管理范式

**Shovel** 是一款面向现代企业安全团队的开源资产测绘平台。通过融合主被动扫描引擎、多模态数据关联分析和智能风险评估模型，我们致力于为企业提供更优雅的资产治理解决方案。

------

### 🚀 核心优势

- **多维资产画像**
  深度整合CMDB/云平台/漏洞库数据源，构建包含2000+指纹规则的资产知识图谱，智能生成空间资产图谱。
- **风险决策中枢**
  内建漏洞优先级算法（CVSS 3.1/EPSS双模评估），结合资产业务价值生成动态风险矩阵。
- **开放架构设计**
  提供标准化OpenAPI和插件API，可实现与主流SIEM/SOAR平台的无缝对接
- **高扩展性插件系统**
  内置高性能管道式插件系统，可灵活地对执行逻辑树进行节点的增删改查，快速将工作流落地。
- **核心 & 中间层分离式架构**
  分离式架构支持灵活分层部署，可快速实现分布式、链式及边缘设备等多种运行模式。

### ⚡ 快速部署

```
# 使用Docker-Compose启动标准集群
git clone https://github.com/your-repo/shovel.git && cd shovel/deploy
docker-compose -f standalone.yml up -d

# 访问管理界面
echo "控制台地址: http://$(curl -s ifconfig.me):8000"
```

[![集成演示](https://img.shields.io/badge/-%E5%9C%A8%E7%BA%BF%E6%BC%94%E7%A4%BA%E7%B3%BB%E7%BB%9F-blue)](https://demo.shovel.com/)
*默认管理员账号：[admin@shovel.local](mailto:admin@shovel.local) / shovel_2024*



### 🧩 扩展生态

我们提供以下扩展能力：

| 模块类型     | 开发示例              | 应用场景         |
| :----------- | :-------------------- | :--------------- |
| 扫描插件     | GitHub监控插件        | 代码仓库资产发现 |
| 解析器       | Shodan数据解析器      | 互联网暴露面分析 |
| 处置动作     | Jira漏洞工单自动创建  | 漏洞闭环管理     |
| 数据源适配器 | AWS Inspector数据对接 | 云原生资产治理   |
ddd
### 🌱 开源生态建设

我们相信安全需要共同智慧：

- 代码提交遵循 [Commitizen规范](https://commitizen-tools.github.io/commitizen/)
- 使用ESLint+Prettier维护代码风格一致性

欢迎通过[讨论区](https://github.com/your-repo/shovel/discussions)参与架构设计讨论，年度贡献者将受邀加入核心开发者小组。
