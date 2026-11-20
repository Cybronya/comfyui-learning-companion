---
name: text_to_image_video_lora_sampler_98
type: Text To Image
frequency: 9
level: strong
coverage: 0.869667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MINIMAX多参官方加速工作流角色一致性图生视频热门IP_2087415478531743745.json, 视频生成/图生视频/MiniMax H3超燃角色PV制作｜人物特效美少女_2095264146601365505.json, 视频生成/图生视频/MiniMaxH3双角色指定背景3图生视频加速版｜图生视频_2089717936046043138.json, 视频生成/图生视频/Minimax H3 高动态打斗模型｜更稳更有冲击力_2096914596027260929.json, 视频生成/图生视频/Minimax H3三图参考无参考音｜图生视频多图参考_2089732304192237570.json, 视频生成/图生视频/Minimax H3双图参考双参考音｜图生视频多模态参考_2089737749720031234.json, 视频生成/图生视频/Minimax H3双图参考无参考音｜图生视频多图参考_2089736461087232001.json, 视频生成/图生视频/Minimax-H3多参长视频736p直出｜原版图生视频工作流_2097088563040051202.json, 视频生成/图生视频/多参生成视频工作流｜多图参考生视频通用稳定版_2113978436757843969.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_98

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MINIMAX多参官方加速工作流角色一致性图生视频热门IP_2087415478531743745.json、视频生成/图生视频/MiniMax H3超燃角色PV制作｜人物特效美少女_2095264146601365505.json、视频生成/图生视频/MiniMaxH3双角色指定背景3图生视频加速版｜图生视频_2089717936046043138.json、视频生成/图生视频/Minimax H3 高动态打斗模型｜更稳更有冲击力_2096914596027260929.json、视频生成/图生视频/Minimax H3三图参考无参考音｜图生视频多图参考_2089732304192237570.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `MiniMaxH3SigmaShift` —— 7/9 个有
- `INTConstant` —— 4/9 个有
- `ModelAttentionBackend` —— 4/9 个有
- `LoadAudio` —— 3/9 个有
- `LoraLoaderBypassModelOnly` —— 2/9 个有
- `ModelPreviewOverrideKJ` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `Display Any (rgthree)` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LoadVideoUI` —— 1/9 个有
- `MiniMaxH3MotionContext` —— 1/9 个有
- `MiniMaxH3MotionContextTrim` —— 1/9 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `SimpleCalculatorKJ` —— 1/9 个有
- `SolAttnMiniMax` —— 1/9 个有
- `StringReplace` —— 1/9 个有
- `TextGenerate` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
