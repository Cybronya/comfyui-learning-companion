---
name: unknown_workflow_video_lora_sampler_466
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.604857
common_nodes: [CLIPVisionLoader, CR Prompt Text, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/定制专用-动作迁移工作流（Wan采样器版）-单路 ViTPose+Draw ViT Pose标准方案_2051347806027296770.json, 视频生成/图生视频/本地开源免费，巴西funk摇僵尸版_2055572704480243714.json, 视频生成/图生视频/本地开源免费，拿破仑进行曲_2056626842236440577.json, 视频生成/图生视频/本地开源免费，杀青梗_2054219479617425409.json, 视频生成/图生视频/本地开源免费，越南鼓捣蒜舞_2055312593698467841.json, 视频生成/图生视频/本地开源免费，香菜摇5_2054476626561388545.json, 视频生成/图生视频/漫剧图生视频remixv1_2069226848269201409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_466

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/定制专用-动作迁移工作流（Wan采样器版）-单路 ViTPose+Draw ViT Pose标准方案_2051347806027296770.json、视频生成/图生视频/本地开源免费，巴西funk摇僵尸版_2055572704480243714.json、视频生成/图生视频/本地开源免费，拿破仑进行曲_2056626842236440577.json、视频生成/图生视频/本地开源免费，杀青梗_2054219479617425409.json、视频生成/图生视频/本地开源免费，越南鼓捣蒜舞_2055312593698467841.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DrawViTPose`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `JWInteger` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `VHS_VideoInfoSource` —— 6/7 个有
- `GetImageRangeFromBatch` —— 4/7 个有
- `FlashVSR_SM_KSampler` —— 3/7 个有
- `FlashVSR_SM_Model` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `easy indexAnything` —— 2/7 个有
- `ImageScale` —— 1/7 个有
- `Int` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有
- `easy imageCount` —— 1/7 个有
- `ttN float` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.75832e+09 | 4.59823e+08 - 1.87794e+09 | 3 | 53% |
| Prompt 约束强度(CFG) | randomize | - | 3 | 100% |
| 采样算法 | 2 | 2 - 2 | 3 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.75832e+09，观测区间 4.59823e+08 - 1.87794e+09，3 个样本
- Prompt 约束强度(CFG) 最常用 randomize，3 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，3 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.87794e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
