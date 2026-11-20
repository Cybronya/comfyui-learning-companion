---
name: unknown_workflow_video_lora_vae_5
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.773125
common_nodes: [Any Switch (rgthree), Fast Groups Muter (rgthree), GetImagesFromBatchIndexed, GetVideoComponents, Int, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PreviewImage, SimpleMath+, VHS_LoadVideo, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, easy framesEditor, easy int, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization, workflow>wanAnimate 采样, workflow>图像拼合, workflow>背景与主体遮罩, workflow>获取对象遮罩, workflow>角色图加序号, workflow>面部与姿势检测]
problems: []
missing: []
members: [平台全量/游戏影视多人二创 · 多角色替换最终整合版（首帧多视角自由切换）_2013481466935648257.json, 平台全量/游戏影视多人二创 · 多角色替换最终整合版（首帧多视角自由切换）_2013975796729257985.json, 平台全量/游戏影视多人二创 · 第二步多角色替换，帧、图融合版（已修复）_2032765199777800194.json, 平台全量/视频二创多角色替换Wan Animate+OneToAll+Same3+SeedVR2.5_1999081169197166594.json, 平台全量/超好用🔥视频二创多角色替换-稳定丝滑_2046866742852460546.json, 数字人/数字人/游戏影视多人二创 · 第二步多人物角色替换（已知问题已修复）_2002697580251344898.json, 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换影视多人二创多角色替换V2_2010224538218401794.json, 视频生成/图生视频/影视二创系列 · 多角色主体替换_1999055940060147714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_5

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/游戏影视多人二创 · 多角色替换最终整合版（首帧多视角自由切换）_2013481466935648257.json、平台全量/游戏影视多人二创 · 多角色替换最终整合版（首帧多视角自由切换）_2013975796729257985.json、平台全量/游戏影视多人二创 · 第二步多角色替换，帧、图融合版（已修复）_2032765199777800194.json、平台全量/视频二创多角色替换Wan Animate+OneToAll+Same3+SeedVR2.5_1999081169197166594.json、平台全量/超好用🔥视频二创多角色替换-稳定丝滑_2046866742852460546.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 8 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
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
- `CreateVideo` —— 5/8 个有
- `LoadVideo` —— 5/8 个有
- `MuyeLoadImage` —— 5/8 个有
- `SaveImage` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `WanVideoSetBlockSwap` —— 5/8 个有
- `WanVideoSetLoRAs` —— 5/8 个有
- `easy blocker` —— 5/8 个有
- `easy indexAnything` —— 5/8 个有
- `LoadImage` —— 3/8 个有
- `LoadVideoWithFilename` —— 3/8 个有
- `PoseDetectionOneToAllAnimation` —— 3/8 个有
- `SaveVideoRGBA` —— 3/8 个有
- `Label (rgthree)` —— 2/8 个有
- `RTXVideoSuperResolution` —— 2/8 个有
- `WanVideoLoraSelect` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
