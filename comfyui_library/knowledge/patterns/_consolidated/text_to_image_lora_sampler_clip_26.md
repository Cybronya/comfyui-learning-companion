---
name: text_to_image_lora_sampler_clip_26
type: Text To Image
frequency: 20
level: strong
coverage: 0.88015
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/9参考MINIMAX-H3数字人_2086538496143089666.json, 数字人/数字人/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086193213840384002.json, 视频生成/图生视频/10Eros-Max Minimax BF16超级融合参考生视频-高质量加速版TEST3_2087401342334758913.json, 视频生成/图生视频/48GB高配版6倍加速参考生视频｜MiniMax H3图生视频工作流_2088219969338302466.json, 视频生成/图生视频/4步加速官方Skills提示词模板多参｜MINIMAX-H3图生视频工作流_2087201189288038401.json, 视频生成/图生视频/4步多图自用提速｜H3图生视频快速参考生成_2089040496692916225.json, 视频生成/图生视频/H3多宫格稳定出片（加速版）MiniMax_2085453124881444865.json, 视频生成/图生视频/H3开源加速版多参文生视频 多宫格稳定出片加速_2099191757274701825.json, 视频生成/图生视频/H3开源加速版多参文生视频 多宫格稳定出片加速_2099565615915819009.json, 视频生成/图生视频/H3开源加速版多参文生视频 多宫格稳定出片加速版_2099209110116982786.json, 视频生成/图生视频/H3开源加速版多参文生视频 多宫格稳定出片加速版_2099588153697988609.json, 视频生成/图生视频/H3稳定加速版整合打斗和脸部修复Lora_2100265879845040129.json, 视频生成/图生视频/MiniMax H3全能参考工作流 多模态输入视频生成_2105367688095821826.json, 视频生成/图生视频/MiniMax H3稳定加速版 整合脸部修复Lora高动态场景适配_2098641262172794881.json, 视频生成/图生视频/MiniMax H3稳定加速版｜打斗脸部修复lora整合_2098767286873182210.json, 视频生成/图生视频/Minimax H3多宫格加速版｜开源海螺多参出片｜漫剧短剧稳定量产_2102631344886075393.json, 视频生成/图生视频/MinimaxH3开源版全能多参｜视频参考标准加速集合版_2095262567538192386.json, 视频生成/图生视频/开源稳定加速版全能参考｜MiniMax H3支持自定义音频图生视频_2091285576120102913.json, 视频生成/文生视频/MiNiMaxH3全能参考文生视频图生视频视频生视频普通加速版_2088368737501143041.json, 视频生成/文生视频/全能参考文生图生视频生视频｜MiNiMaxH3视频生成工作流_2088334930496548865.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（数字人/数字人/9参考MINIMAX-H3数字人_2086538496143089666.json、数字人/数字人/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086193213840384002.json、视频生成/图生视频/10Eros-Max Minimax BF16超级融合参考生视频-高质量加速版TEST3_2087401342334758913.json、视频生成/图生视频/48GB高配版6倍加速参考生视频｜MiniMax H3图生视频工作流_2088219969338302466.json、视频生成/图生视频/4步加速官方Skills提示词模板多参｜MINIMAX-H3图生视频工作流_2087201189288038401.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 19/20 个有
- `SaveVideo` —— 19/20 个有
- `KSamplerSelect` —— 18/20 个有
- `MiniMaxH3ReferenceToVideo` —— 15/20 个有
- `VHS_VideoCombine` —— 15/20 个有
- `LoadAudio` —— 12/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/20 个有
- `PathchSageAttentionKJ` —— 10/20 个有
- `LoraLoaderBypassModelOnly` —— 9/20 个有
- `EasyCache` —— 8/20 个有
- `MiniMaxH3AudioConditioningT8` —— 8/20 个有
- `Fast Groups Bypasser (rgthree)` —— 7/20 个有
- `SaveImage` —— 7/20 个有
- `ModelPatchTorchSettings` —— 6/20 个有
- `VHS_LoadVideo` —— 6/20 个有
- `MiniMaxH3DualClockSamplerT8` —— 5/20 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/20 个有
- `AudioCrop` —— 3/20 个有
- `MiniMaxH3AVDecodeT8` —— 3/20 个有
- `忽略多组孤海` —— 3/20 个有
- `ImageResizeKJv2` —— 1/20 个有
- `JWString` —— 1/20 个有
- `JoinStrings` —— 1/20 个有
- `Label (rgthree)` —— 1/20 个有
- `LoadVideo` —— 1/20 个有
- `MiniMaxH3BlockCacheT8` —— 1/20 个有
- `SpectrumSDXL` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（30/20 个样本）：Steps较低可能导致细节不足
