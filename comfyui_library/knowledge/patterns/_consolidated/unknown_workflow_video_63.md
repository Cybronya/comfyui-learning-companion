---
name: unknown_workflow_video_63
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.783333
common_nodes: [Any Switch (rgthree), Fast Groups Muter (rgthree), GetImagesFromBatchIndexed, GetVideoComponents, Int, LoadImage, LoadVideoWithFilename, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, PreviewImage, SimpleMath+, VHS_LoadVideo, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, easy framesEditor, easy int, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization, workflow>wanAnimate 采样, workflow>图像拼合, workflow>背景与主体遮罩, workflow>获取对象遮罩, workflow>角色图加序号, workflow>面部与姿势检测]
problems: []
missing: []
members: [视频生成/图生视频/2000558063344025601.json, 视频生成/图生视频/1999055940060147714.json, 视频生成/图生视频/2004211768807354370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_63

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2000558063344025601.json、视频生成/图生视频/1999055940060147714.json、视频生成/图生视频/2004211768807354370.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `Int`
- `LoadImage`
- `LoadVideoWithFilename`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `easy framesEditor`
- `easy int`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`
- `workflow>wanAnimate 采样`
- `workflow>图像拼合`
- `workflow>背景与主体遮罩`
- `workflow>获取对象遮罩`
- `workflow>角色图加序号`
- `workflow>面部与姿势检测`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/3 个有
- `SaveVideoRGBA` —— 2/3 个有
- `workflow>WanAnimate KJ加载器` —— 2/3 个有
- `CreateVideo` —— 1/3 个有
- `LoadWanVideoT5TextEncoder` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `WanVideoBlockSwap` —— 1/3 个有
- `WanVideoLoraSelectMulti` —— 1/3 个有
- `WanVideoModelLoader` —— 1/3 个有
- `WanVideoVAELoader` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
