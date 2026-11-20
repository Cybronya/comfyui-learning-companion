---
name: unknown_workflow_video_sampler_clip_188
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.594333
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, Fast Groups Bypasser (rgthree), JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy anythingIndexSwitch, easy showAnything]
problems: []
missing: []
members: [平台全量/图生视频_Wan2.2_Dasiwa+提示词自动手动切换_1995379775025950721.json, 视频生成/图生视频/Wan2.2 Remix  V3.0  图生视频 自动提示词_2034288165581758466.json, 视频生成/图生视频/Wan2.2_I2V_Remix V2.1+PainterI2V+VBVR奖励lora 图生视频_2025905016736845825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_188

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/图生视频_Wan2.2_Dasiwa+提示词自动手动切换_1995379775025950721.json、视频生成/图生视频/Wan2.2 Remix  V3.0  图生视频 自动提示词_2034288165581758466.json、视频生成/图生视频/Wan2.2_I2V_Remix V2.1+PainterI2V+VBVR奖励lora 图生视频_2025905016736845825.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `TT_img_enc_v2` —— 2/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `Int` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `SaveLatent` —— 1/3 个有
- `WanImageToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
