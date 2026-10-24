---
name: unknown_workflow_video_sampler_clip_161
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8435
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/wan（Remix_smooth_dasiwa）+PainterI2V图生视频手动提示词工作流V1_2016325482970615810.json, 视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json, 视频生成/文生视频/图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145.json, 音频生成/音频生成/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028776980736380930.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan（Remix_smooth_dasiwa）+PainterI2V图生视频手动提示词工作流V1_2016325482970615810.json、视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json、视频生成/文生视频/图生视频自动提示词 Remix V2.1+PainterI2V 一致性加强版_2037406985737478145.json、音频生成/音频生成/Remix V2.1图生视频V1（UnifiedReward+VBVR逻辑加强）_2028776980736380930.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `Float` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ImageFromBatch+` —— 2/4 个有
- `PainterI2V` —— 2/4 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 2/4 个有
- `RunningHub Deepcleaner` —— 2/4 个有
- `easy anythingIndexSwitch` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `ColorMatch` —— 1/4 个有
- `FILM VFI` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Pick From Batch (mtb)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `WanImageToVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
