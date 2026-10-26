---
name: unknown_workflow_video_lora_sampler_267
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.740333
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetNode, ImageBatchExtendWithOverlap, ImageFromBatch+, JDCN_StringToList, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, SetNode, Text, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, easy indexAnything]
problems: []
missing: []
members: [视频生成/图生视频/漫剧分镜视频1_2028866399321460738.json, 视频生成/图生视频/漫剧分镜视频2_2028877052505497602.json, 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206584266399745.json, 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206599869206529.json, 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027227746778226690.json, 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027240499706335233.json, 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027250620972929026.json, 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027258275158302721.json, 视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027266835749543937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_267

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/漫剧分镜视频1_2028866399321460738.json、视频生成/图生视频/漫剧分镜视频2_2028877052505497602.json、视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206584266399745.json、视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027206599869206529.json、视频生成/图生视频/真人AI分镜视频 Real person AI video リアル人間AIビデオ_2027227746778226690.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageFromBatch+`
- `JDCN_StringToList`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `SetNode`
- `Text`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `easy indexAnything`

**可变部分**（部分 workflow 才有）：
- `LoaderGGUF` —— 2/9 个有
- `Load3D` —— 1/9 个有
- `LoadEXR` —— 1/9 个有
- `LoadSRT` —— 1/9 个有
- `Loader` —— 1/9 个有
- `load_GGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
