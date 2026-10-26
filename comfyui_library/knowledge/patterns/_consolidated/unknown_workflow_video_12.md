---
name: unknown_workflow_video_12
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.791286
common_nodes: [GetImagesFromBatchIndexed, GetVideoComponents, Int, LoadVideoWithFilename, OnnxDetectionModelLoader, PreviewImage, VHS_LoadVideo, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization, workflow>wanAnimate 采样, workflow>图像拼合, workflow>背景与主体遮罩, workflow>角色图加序号, workflow>面部与姿势检测]
problems: []
missing: []
members: [数字人/数字人/Wan animate 视频多人替换 影视二创_2000399958677352450.json, 数字人/数字人/Wan animate多人说话稳定版_2001136521040326657.json, 数字人/数字人/【自用】 视频二创多角色替换_2001483028935344129.json, 数字人/数字人/【自用】 视频二创多角色替换_2001500686896513026.json, 视频生成/图生视频/Wan animate多人说话稳定版_2003080671885238273.json, 视频生成/图生视频/多角色替换Wan+Animate+OneToAll+Same3+SeedVR2.5_2000558063344025601.json, 视频生成/图生视频/视频二创-多角色替换Wan Animate+OneToAll+Same3+SeedVR2.5_2004211768807354370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_12

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/Wan animate 视频多人替换 影视二创_2000399958677352450.json、数字人/数字人/Wan animate多人说话稳定版_2001136521040326657.json、数字人/数字人/【自用】 视频二创多角色替换_2001483028935344129.json、数字人/数字人/【自用】 视频二创多角色替换_2001500686896513026.json、视频生成/图生视频/Wan animate多人说话稳定版_2003080671885238273.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `Int`
- `LoadVideoWithFilename`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`
- `workflow>wanAnimate 采样`
- `workflow>图像拼合`
- `workflow>背景与主体遮罩`
- `workflow>角色图加序号`
- `workflow>面部与姿势检测`

**可变部分**（部分 workflow 才有）：
- `SaveVideoRGBA` —— 6/7 个有
- `easy framesEditor` —— 6/7 个有
- `workflow>WanAnimate KJ加载器` —— 6/7 个有
- `workflow>获取对象遮罩` —— 6/7 个有
- `SimpleMath+` —— 5/7 个有
- `easy int` —— 5/7 个有
- `Any Switch (rgthree)` —— 4/7 个有
- `Fast Groups Muter (rgthree)` —— 4/7 个有
- `LoadImage` —— 4/7 个有
- `PoseDetectionOneToAllAnimation` —— 4/7 个有
- `SaveImage` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `RHHiddenNodes` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `easy blocker` —— 1/7 个有
- `easy ifElse` —— 1/7 个有
- `easy indexAnything` —— 1/7 个有
- `workflow>模型加载` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
