---
name: text_to_image_upscale_latent_upscale_lora_2
type: Text To Image
frequency: 22
level: strong
coverage: 0.602864
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json, 视频生成/图生视频/MiniMax H3 Digital Avatars for Video E co数字人视频带货方案_2108634054257111041.json, 视频生成/图生视频/MiniMax H3 Turbo V4｜Realism真人写实参考生视频｜超写实图生视频流_2108004956178567169.json, 视频生成/图生视频/MiniMax H3 多参考生视频 720p｜一采快二采质量高支持特效_2096841455523422209.json, 视频生成/图生视频/MiniMax H3动作迁移2.0史诗强化进阶版，视频生视频动态姿势迁移工具_2103188261547102209.json, 视频生成/图生视频/MiniMax H3动作迁移9分钟出视频，图生视频视频生视频高效产出方案_2103599685733801986.json, 视频生成/图生视频/MiniMax H3动作迁移9分钟出视频，图生视频视频生视频高效产出方案_2103930965801398273.json, 视频生成/图生视频/MiniMax H3多参生视频优化版｜9图3音3视频参考_2095604235936292865.json, 视频生成/图生视频/MiniMax H3多参考生视频 快速高质量图生视频_2098830853072834562.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版 高质量图生视频工具_2099190175938207745.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版｜多图参考更听话，画面更贴需求_2099467720621387777.json, 视频生成/图生视频/MiniMax H3多参考生视频工作流，图生视频多素材融合方案_2103581304431407106.json, 视频生成/图生视频/MiniMax H3多参考生视频快速高质量版｜图生视频速度画质兼得_2099143441149157378.json, 视频生成/图生视频/Minimax H3 Turbo V4 Realism People参考生视频超写实工作流，图生视频_2108259144510828545.json, 视频生成/图生视频/Minimax H3多参考双采｜最强一致性Singularity出视频_2101538998190698498.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采生视频多比例版_2104776734221627394.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采生视频标准版_2104646935444549633.json, 视频生成/图生视频/Singularity最强一致性 Minimax H3多参考双采视频生成_2098283807588839426.json, 视频生成/图生视频/Singularity最强一致性多参考双采生视频处理工具_2101743307100610561.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频王牌版_2104560310488223746.json, 视频生成/文生视频/0906 万象AI+Singularity 新模型｜12秒横屏960分辨率_2096858352113512449.json, 视频生成/文生视频/0906 万象AI+Singularity 新模型｜12秒竖屏960分辨率_2096856463141588993.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json、视频生成/图生视频/MiniMax H3 Digital Avatars for Video E co数字人视频带货方案_2108634054257111041.json、视频生成/图生视频/MiniMax H3 Turbo V4｜Realism真人写实参考生视频｜超写实图生视频流_2108004956178567169.json、视频生成/图生视频/MiniMax H3 多参考生视频 720p｜一采快二采质量高支持特效_2096841455523422209.json、视频生成/图生视频/MiniMax H3动作迁移2.0史诗强化进阶版，视频生视频动态姿势迁移工具_2103188261547102209.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 22 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 21/22 个有
- `LoadAudio` —— 21/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 21/22 个有
- `ResolutionSelector` —— 21/22 个有
- `SetNode` —— 21/22 个有
- `SplitSigmas` —— 21/22 个有
- `VHS_VideoCombine` —— 21/22 个有
- `Text` —— 20/22 个有
- `VHS_LoadVideo` —— 20/22 个有
- `easy float` —— 20/22 个有
- `SaveImage` —— 12/22 个有
- `Lora Loader Stack (rgthree)` —— 9/22 个有
- `SolAttnMiniMax` —— 9/22 个有
- `ModelAttentionBackend` —— 8/22 个有
- `llama_cpp_instruct_adv` —— 3/22 个有
- `llama_cpp_model_loader` —— 3/22 个有
- `llama_cpp_parameters` —— 3/22 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/22 个有
- `ShowText|pysssss` —— 2/22 个有
- `easy cleanGpuUsed` —— 2/22 个有
- `ManualSigmas` —— 1/22 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 1/22 个有
- `MiniMaxH3SigmaShift` —— 1/22 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 1/22 个有
- `PixaromaSaveMp4` —— 1/22 个有
- `PreviewAny` —— 1/22 个有
- `SigmasToFloat` —— 1/22 个有
- `easy int` —— 1/22 个有
- `忽略多组孤海` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（23/22 个样本）：Steps较低可能导致细节不足
