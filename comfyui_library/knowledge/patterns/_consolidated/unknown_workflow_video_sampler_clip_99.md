---
name: unknown_workflow_video_sampler_clip_99
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.7595
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Float, ImageResizeKJv2, ImageScaleBy, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, RunningHub Deepcleaner, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2039903476511150082.json, 视频生成/图生视频/2012167741138018306.json, 视频生成/图生视频/2029118702054023169.json, 视频生成/图生视频/2011779085244047362.json, 视频生成/图生视频/1991472801660018689.json, 音频生成/音频生成/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028776980736380930.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_99

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2039903476511150082.json、视频生成/图生视频/2012167741138018306.json、视频生成/图生视频/2029118702054023169.json、视频生成/图生视频/2011779085244047362.json、视频生成/图生视频/1991472801660018689.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Float`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RunningHub Deepcleaner`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 5/6 个有
- `CR Prompt Text` —— 5/6 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 5/6 个有
- `Pick From Batch (mtb)` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `ColorMatch` —— 4/6 个有
- `ImageFromBatch+` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `PainterI2V` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `RH_LLMAPI_NODE` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `TT_img_enc` —— 2/6 个有
- `TT_img_enc_v2` —— 2/6 个有
- `ConcatTextOfUtils` —— 1/6 个有
- `DuckHideNode` —— 1/6 个有
- `Text` —— 1/6 个有
- `WanImageToVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler_ancestral | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
