---
name: text_to_image_lora_sampler_clip_17
type: Text To Image
frequency: 20
level: strong
coverage: 0.8777
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093430390005518337.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093761824507383810.json, 视频生成/图生视频/开源加速版来了｜海螺H3多宫格角色设计图生视频_2096543788733911041.json, 视频生成/图生视频/开源稳定加速版全能参考｜MiniMax H3支持自定义音频图生视频_2091285576120102913.json, 视频生成/图生视频/海螺H3开源加速多参版｜文生图生视频通吃，短剧漫剧稳定量产_2099487127842148353.json, 视频生成/图生视频/海螺多参漫剧短剧｜h3开源加速版多宫格稳定出片_2092903041468030978.json, 视频生成/图生视频/海螺多参稳定出片｜H3开源加速多宫格漫剧短剧生成_2096321156952453121.json, 视频生成/图生视频/海螺多宫格稳定出片加速｜MiniMax H3开源多参漫剧短剧_2092712378231255041.json, 视频生成/图生视频/漫剧林辰图生视频｜短剧角色动起来 图生视频一键成片_2104102680842039298.json, 视频生成/图生视频/漫剧林辰角色动态演绎 图生视频一键生成流畅画面_2104279422512754690.json, 视频生成/图生视频/短剧漫剧参考图生视频工作流，图生视频短剧制作方案_2103604319982542850.json, 视频生成/图生视频/稳定加速5参考图版｜MiniMax H3全能参考自定义音频_2091200766919925762.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3五参考图音频自定义_2090900087277973505.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3开源支持自定义音频_2091271985484623874.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3支持自定义音频_2092396498217689090.json, 视频生成/图生视频/稳定加速版｜MiniMax H3 全能参考4步加速_2089295207438307330.json, 视频生成/图生视频/音画同步参考工作流｜MiniMax H3角色表演图生视频_2091604729305583617.json, 视频生成/图生视频/音画同步参考生成｜MiniMax H3角色表演图生视频_2091775715330060290.json, 视频生成/文生视频/H3阿里3步加速Lora全能参考速度起飞_2100295935514468353.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/图生视频高质量生成｜MiniMax H3画面细节增强_2096700949896196098.json、视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093430390005518337.json、视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093761824507383810.json、视频生成/图生视频/开源加速版来了｜海螺H3多宫格角色设计图生视频_2096543788733911041.json、视频生成/图生视频/开源稳定加速版全能参考｜MiniMax H3支持自定义音频图生视频_2091285576120102913.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 19/20 个有
- `SaveVideo` —— 19/20 个有
- `VAEDecodeAudio` —— 19/20 个有
- `KSamplerSelect` —— 18/20 个有
- `PrimitiveStringMultiline` —— 15/20 个有
- `MiniMaxH3ReferenceToVideo` —— 13/20 个有
- `VHS_VideoCombine` —— 12/20 个有
- `PathchSageAttentionKJ` —— 11/20 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/20 个有
- `LoadAudio` —— 8/20 个有
- `MiniMaxH3AudioConditioningT8` —— 7/20 个有
- `ModelPatchTorchSettings` —— 7/20 个有
- `EasyCache` —— 6/20 个有
- `Fast Groups Bypasser (rgthree)` —— 6/20 个有
- `LoraLoaderBypassModelOnly` —— 6/20 个有
- `MiniMaxH3DualClockSamplerT8` —— 6/20 个有
- `CR Text` —— 3/20 个有
- `SaveImage` —— 3/20 个有
- `CR Prompt Text` —— 2/20 个有
- `SpectrumSDXLBatch` —— 2/20 个有
- `Label (rgthree)` —— 1/20 个有
- `MiniMaxH3AVDecodeT8` —— 1/20 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/20 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/20 个有
- `RTXVideoSuperResolution` —— 1/20 个有
- `SolAttnMiniMax` —— 1/20 个有
- `SpectrumApplyMiniMaxH3` —— 1/20 个有
- `VHS_LoadVideo` —— 1/20 个有

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
| Steps较低可能导致细节不足 | 28/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（28/20 个样本）：Steps较低可能导致细节不足
