---
name: text_to_image_lora_sampler_clip_165
type: Text To Image
frequency: 11
level: strong
coverage: 0.816636
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/首尾帧参考生视频｜MiniMax H3 8步LoRa+Sage双重加速特效_2089827009160638465.json, 视频生成/图生视频/首尾帧图生视频｜minimaxH3 FL2VA开源直出_2093791140687466498.json, 视频生成/图生视频/首尾帧提示词自动扩写T8｜MinimaxH3角色一致性分镜图生视频_2091163950061809666.json, 视频生成/图生视频/首尾帧生视频In8加速版｜Minimax H3图生视频工作流_2088117119526465537.json, 视频生成/图生视频/首尾帧生视频版本｜傲雪AIGC MiniMax+H3角色一致性表演_2094716870489370626.json, 视频生成/图生视频/首尾帧视频图生成｜Minimax H3图生视频衔接_2095508493355806721.json, 视频生成/文生视频/Fastvideo H3快速文生视频｜ComfyUI加速生成_2095222013941080065.json, 视频生成/文生视频/LightX2V Turbo加速｜MiniMax H3文生图生视频生视频工作流_2087187099337445378.json, 视频生成/文生视频/MiniMax H3文生视频电商带货｜手机取物换装创意视频_2108095483951538177.json, 视频生成/文生视频/Minimax-H3VDN-R2V三模式生成｜RH在线流直跑_2097156284557643777.json, 视频生成/文生视频/Minimax-H3VDN-R2V视频生成｜RH在线流工作流制作_2097073901951086594.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_165

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/首尾帧参考生视频｜MiniMax H3 8步LoRa+Sage双重加速特效_2089827009160638465.json、视频生成/图生视频/首尾帧图生视频｜minimaxH3 FL2VA开源直出_2093791140687466498.json、视频生成/图生视频/首尾帧提示词自动扩写T8｜MinimaxH3角色一致性分镜图生视频_2091163950061809666.json、视频生成/图生视频/首尾帧生视频In8加速版｜Minimax H3图生视频工作流_2088117119526465537.json、视频生成/图生视频/首尾帧生视频版本｜傲雪AIGC MiniMax+H3角色一致性表演_2094716870489370626.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 10/11 个有
- `LoadImage` —— 9/11 个有
- `MiniMaxH3ImageToVideo` —— 9/11 个有
- `ResolutionSelector` —— 9/11 个有
- `VHS_VideoCombine` —— 7/11 个有
- `GetNode` —— 5/11 个有
- `PrimitiveStringMultiline` —— 5/11 个有
- `SetNode` —— 5/11 个有
- `CreateVideo` —— 4/11 个有
- `ImageResizeKJv2` —— 4/11 个有
- `ModelAttentionBackend` —— 4/11 个有
- `SaveVideo` —— 4/11 个有
- `Text` —— 4/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/11 个有
- `MiniMaxH3SigmaShift` —— 3/11 个有
- `PathchSageAttentionKJ` —— 3/11 个有
- `StringConcatenate` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `MiniMaxChunkFeedForward` —— 2/11 个有
- `MiniMaxH3ReferenceToVideo` —— 2/11 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 2/11 个有
- `MiniMaxLowVRAMAttention` —— 2/11 个有
- `ModelPatchTorchSettings` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `SolAttnPatch` —— 2/11 个有
- `ImageResize+` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
