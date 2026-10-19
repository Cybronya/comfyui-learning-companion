---
name: text_to_image_lora_sampler_clip_13
type: Text To Image
frequency: 22
level: strong
coverage: 0.878545
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/9参考MINIMAX-H3数字人_2086538496143089666.json, 数字人/数字人/MiniMax H3多图参考官方提示词模板｜提速40%无劣化真人短剧剧情演绎数字人_2090475334801125378.json, 数字人/数字人/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086193213840384002.json, 数字人/数字人/官方提示词模板提速40%｜MiniMax H3多图参考真人短剧演绎_2090193856364109826.json, 视频生成/图生视频/10Eros-Max Minimax BF16超级融合参考生视频-高质量加速版TEST3_2087401342334758913.json, 视频生成/图生视频/H3多宫格稳定出片（加速版）MiniMax_2085453124881444865.json, 视频生成/图生视频/H3开源加速版多参文生视频 多宫格稳定出片加速_2099191757274701825.json, 视频生成/图生视频/H3开源加速版多参文生视频 多宫格稳定出片加速_2099565615915819009.json, 视频生成/图生视频/H3开源加速版多参文生视频 多宫格稳定出片加速版_2099209110116982786.json, 视频生成/图生视频/H3开源加速版多参文生视频 多宫格稳定出片加速版_2099588153697988609.json, 视频生成/图生视频/H3开源加速版多参文生视频图生视频多宫格稳定出片漫剧制作方案_2106491061026779138.json, 视频生成/图生视频/H3开源加速版多参文生视频图生视频，多宫格稳定出片适用于漫剧 制作_2102835082758279169.json, 视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧 多宫格稳定出片方案_2106478696466046978.json, 视频生成/图生视频/H3开源加速版海螺多参文生视频图生视频漫剧短剧多宫格稳定出片方案_2106506103612858369.json, 视频生成/图生视频/MiniMax H3全能参考工作流 多模态输入视频生成_2105367688095821826.json, 视频生成/图生视频/MiniMax H3开源加速多宫格稳定出片｜海螺多参漫剧短剧人物特效角色设计图生视频_2089710412790067202.json, 视频生成/图生视频/MiniMax H3开源加速版｜海螺多参多宫格稳定出片｜漫剧短剧加速搞定_2102600651598553090.json, 视频生成/图生视频/MiniMax H3稳定加速版 整合脸部修复Lora高动态场景适配_2098641262172794881.json, 视频生成/图生视频/MiniMax H3稳定加速版｜打斗脸部修复lora整合_2098767286873182210.json, 视频生成/图生视频/MiniMax h3开源加速版海螺多参文生视频图生视频漫剧短剧视频H3多宫格稳定出片加速版_2085308700373381121.json, 视频生成/文生视频/H3开源加速版多参文生视频图生视频多宫格稳定出片漫剧制作方案_2106491061026779138.json, 视频生成/文生视频/H3开源加速版多参文生视频图生视频，多宫格稳定出片适用于漫剧_制作_2106170895910924289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（数字人/数字人/9参考MINIMAX-H3数字人_2086538496143089666.json、数字人/数字人/MiniMax H3多图参考官方提示词模板｜提速40%无劣化真人短剧剧情演绎数字人_2090475334801125378.json、数字人/数字人/minimax开源版中文锁定语音H3稳定4步lora加速版优化版图生视频_2086193213840384002.json、数字人/数字人/官方提示词模板提速40%｜MiniMax H3多图参考真人短剧演绎_2090193856364109826.json、视频生成/图生视频/10Eros-Max Minimax BF16超级融合参考生视频-高质量加速版TEST3_2087401342334758913.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：88%

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
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 21/22 个有
- `CreateVideo` —— 20/22 个有
- `PrimitiveStringMultiline` —— 20/22 个有
- `SaveVideo` —— 20/22 个有
- `孤海注释` —— 20/22 个有
- `MiniMaxH3ReferenceToVideo` —— 19/22 个有
- `VHS_VideoCombine` —— 19/22 个有
- `PathchSageAttentionKJ` —— 18/22 个有
- `EasyCache` —— 17/22 个有
- `Fast Groups Bypasser (rgthree)` —— 15/22 个有
- `ModelPatchTorchSettings` —— 14/22 个有
- `SaveImage` —— 12/22 个有
- `LoadAudio` —— 5/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/22 个有
- `LoraLoaderBypassModelOnly` —— 4/22 个有
- `EmptyImage` —— 3/22 个有
- `MiniMaxH3AudioConditioningT8` —— 3/22 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/22 个有
- `PreviewImage` —— 3/22 个有
- `GetImageSize` —— 2/22 个有
- `ResizeImageMaskNode` —— 2/22 个有
- `Textbox` —— 2/22 个有
- `VHS_LoadVideo` —— 2/22 个有
- `JWString` —— 1/22 个有
- `JoinStrings` —— 1/22 个有
- `Label (rgthree)` —— 1/22 个有
- `LoadVideo` —— 1/22 个有
- `MiniMaxH3BlockCacheT8` —— 1/22 个有

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
| Steps较低可能导致细节不足 | 48/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（48/22 个样本）：Steps较低可能导致细节不足
