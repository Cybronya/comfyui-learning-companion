---
name: text_to_image_video_lora_sampler_61
type: Text To Image
frequency: 11
level: strong
coverage: 0.881727
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyLTXVLatentVideo, EmptyLatentImage, INTConstant, JjkText, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LoraLoaderModelOnly, LowVRAMCheckpointLoader, ManualSigmas, RH_Captioner, RandomNoise, SamplerCustomAdvanced, StringReplace, Text, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/3分镜图生视频｜image2+LTX-MSR多参运镜，出片更有戏_2099909158635139074.json, 视频生成/图生视频/3分镜多参图生视频｜image2+LTX-MSR组合生成_2095484514092015618.json, 视频生成/图生视频/Image2加LTX多参数三分镜图生视频 多角色分镜创作_2099916907792130050.json, 视频生成/图生视频/LTX-MSR多参3分镜图生视频image2_2087478149268459522.json, 视频生成/图生视频/Licon-MSR长镜头版｜Ltx2.3 视频运镜_2089290894364205058.json, 视频生成/图生视频/Licon-MSR长镜头版｜Ltx2.3图生视频生成_2093239106930307073.json, 视频生成/图生视频/Ltx2.3 Licon-MSR 长镜头版本｜图生视频电影级运镜_2096822173271945218.json, 视频生成/图生视频/Ltx2.3 Licon-MSR长镜头版图生视频处理工作流_2101364005368582146.json, 视频生成/图生视频/image2+LTX-MSR多参3分镜｜图生视频工作流_2095207789642731522.json, 视频生成/图生视频/image2+LTX-MSR多参三分镜｜图生视频连续衔接直出_2091245168753201153.json, 视频生成/图生视频/图生视频长镜头利器｜Ltx2.3 Licon-MSR长镜头版本_2101120778602373122.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/3分镜图生视频｜image2+LTX-MSR多参运镜，出片更有戏_2099909158635139074.json、视频生成/图生视频/3分镜多参图生视频｜image2+LTX-MSR组合生成_2095484514092015618.json、视频生成/图生视频/Image2加LTX多参数三分镜图生视频 多角色分镜创作_2099916907792130050.json、视频生成/图生视频/LTX-MSR多参3分镜图生视频image2_2087478149268459522.json、视频生成/图生视频/Licon-MSR长镜头版｜Ltx2.3 视频运镜_2089290894364205058.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `INTConstant`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `StringReplace`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/11 个有
- `RH_RhartImageG2ImageToImage` —— 6/11 个有
- `TextConcatenate_UTK` —— 6/11 个有
- `easy imageSplitGrid` —— 6/11 个有
- `easy indexAnything` —— 6/11 个有
- `GoogleTranslator` —— 5/11 个有
- `ImageConcatMulti` —— 5/11 个有
- `SaveImage` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
