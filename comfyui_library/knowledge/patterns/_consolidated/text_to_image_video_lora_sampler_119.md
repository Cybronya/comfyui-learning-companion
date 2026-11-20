---
name: text_to_image_video_lora_sampler_119
type: Text To Image
frequency: 8
level: strong
coverage: 0.77825
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/全能插件加速版minimaxH3数字人工作流_2087430084268482561.json, 视频生成/图生视频/商业级360度环绕镜头展示｜产品级运镜一镜到底_2111325834421293058.json, 视频生成/文生视频/8步768p加速新版 MiniMax H3 单采高质量文生视频_2094171689625153537.json, 视频生成/文生视频/8步768p加速新版｜MiniMax H3单采高质量三模视频_2094310836981551107.json, 视频生成/文生视频/Minimax-H3VDN-R2V三模式生成｜RH在线流直跑_2097156284557643777.json, 视频生成/文生视频/Minimax-H3VDN-R2V视频生成｜RH在线流工作流制作_2097073901951086594.json, 视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频生成_2093790080652627970.json, 视频生成/文生视频/六宫格生视频｜minimax h3文生图生视频直出_2093456500986568705.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_119

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/全能插件加速版minimaxH3数字人工作流_2087430084268482561.json、视频生成/图生视频/商业级360度环绕镜头展示｜产品级运镜一镜到底_2111325834421293058.json、视频生成/文生视频/8步768p加速新版 MiniMax H3 单采高质量文生视频_2094171689625153537.json、视频生成/文生视频/8步768p加速新版｜MiniMax H3单采高质量三模视频_2094310836981551107.json、视频生成/文生视频/Minimax-H3VDN-R2V三模式生成｜RH在线流直跑_2097156284557643777.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 7/8 个有
- `VAEDecodeAudio` —— 7/8 个有
- `MiniMaxH3SigmaShift` —— 6/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `LoadImage` —— 5/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/8 个有
- `ModelPreviewOverrideKJ` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `ComfyMathExpression` —— 4/8 个有
- `GetNode` —— 4/8 个有
- `MiniMaxH3ReferenceToVideo` —— 4/8 个有
- `MiniMaxH3Unified` —— 4/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `MiniMaxChunkFeedForward` —— 3/8 个有
- `MiniMaxLowVRAMAttention` —— 3/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `CR Text` —— 2/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 2/8 个有
- `ModelPatchTorchSettings` —— 2/8 个有
- `SolAttnPatch` —— 2/8 个有
- `StringConcatenate` —— 2/8 个有
- `Label (rgthree)` —— 1/8 个有
- `MemoryCleaner` —— 1/8 个有
- `MiniMaxH3AVDecodeT8` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
