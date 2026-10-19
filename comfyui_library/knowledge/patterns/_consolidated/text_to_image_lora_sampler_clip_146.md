---
name: text_to_image_lora_sampler_clip_146
type: Text To Image
frequency: 7
level: strong
coverage: 0.852714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/桌面女友互动形象生成，图生图转图生视频方案_2111234634200735745.json, 视频生成/图生视频/桌面女友图生视频｜暖心陪伴向AI视频一键生成_2111272944059117569.json, 视频生成/文生视频/DiT int8加速｜MiniMax H3 FL2VA开源版图像音频参考生视频_2090821057673519105.json, 视频生成/文生视频/H3文生视频8步工作流 高效视频生成工具_2100289449610534913.json, 视频生成/文生视频/MINIMAX-H3文生视频工作流｜图生视频双模式｜短视频创作提效_2101872099584466946.json, 视频生成/文生视频/MiniMax H3文生视频 官方全模态立体声生成_2098835843896139777.json, 视频生成/文生视频/Minimax文生视频T2V工作流，加写实LoRA开关文生视频方案_2106872283892637697.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_146

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/桌面女友互动形象生成，图生图转图生视频方案_2111234634200735745.json、视频生成/图生视频/桌面女友图生视频｜暖心陪伴向AI视频一键生成_2111272944059117569.json、视频生成/文生视频/DiT int8加速｜MiniMax H3 FL2VA开源版图像音频参考生视频_2090821057673519105.json、视频生成/文生视频/H3文生视频8步工作流 高效视频生成工具_2100289449610534913.json、视频生成/文生视频/MINIMAX-H3文生视频工作流｜图生视频双模式｜短视频创作提效_2101872099584466946.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 5/7 个有
- `ComfySwitchNode` —— 4/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `GetImageSize` —— 2/7 个有
- `ImageCompositeMasked` —— 2/7 个有
- `ImageScale` —— 2/7 个有
- `ImageScaleBy` —— 2/7 个有
- `Int` —— 2/7 个有
- `ManualSigmas` —— 2/7 个有
- `QwenImage21Cache` —— 2/7 个有
- `SamplerCustom` —— 2/7 个有
- `SolAttnPatch` —— 2/7 个有
- `TextEncodeQwenImage21` —— 2/7 个有
- `GetNode` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `Wan_Organic_Skin` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
