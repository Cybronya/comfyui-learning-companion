---
name: text_to_image_lora_sampler_clip_274
type: Text To Image
frequency: 8
level: strong
coverage: 0.76575
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/首尾帧图文一键生视频｜MiniMax H3加速版数字人_2095958370124656641.json, 视频生成/图生视频/首尾帧生视频！加速版MiniMaxH3转场特效数字人图生视频_2085455030794145794.json, 视频生成/文生视频/24GB通用版6倍加速参考生视频｜MiniMax H3文生图生视频生视频工作流_2087179601289236482.json, 视频生成/文生视频/48GB高配版6倍加速参考生视频｜MiniMax H3文生图生视频工作流_2087157477258383362.json, 视频生成/文生视频/H3全能参考生视频MiniMax视频生视频图生视频_2086209628857266177.json, 视频生成/文生视频/开源加速版MiniMax h3海螺多参文生视频图生视频音频参考_2085178835024306178.json, 视频生成/视频生视频/免手写提示词 MiniMax H3角色一致性图生视频人物替换_2106531233084821505.json, 视频生成/视频生视频/智能反推提示词免手写 Minimax H3角色一致性人物替换图生视频方案_2106158187798941698.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_274

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/首尾帧图文一键生视频｜MiniMax H3加速版数字人_2095958370124656641.json、视频生成/图生视频/首尾帧生视频！加速版MiniMaxH3转场特效数字人图生视频_2085455030794145794.json、视频生成/文生视频/24GB通用版6倍加速参考生视频｜MiniMax H3文生图生视频生视频工作流_2087179601289236482.json、视频生成/文生视频/48GB高配版6倍加速参考生视频｜MiniMax H3文生图生视频工作流_2087157477258383362.json、视频生成/文生视频/H3全能参考生视频MiniMax视频生视频图生视频_2086209628857266177.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoadImage`
- `LoraLoaderModelOnly`
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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 7/8 个有
- `EasyCache` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `ImageResizeKJv2` —— 3/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `LoadAudio` —— 2/8 个有
- `MiniMaxH3ImageToVideo` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `RHHiddenNodes` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `AILab_QwenVL_Advanced` —— 1/8 个有
- `DF_Int_to_Float` —— 1/8 个有
- `Image Stitch` —— 1/8 个有
- `ImageScaleDownToSize` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `ShowAnything|Mie` —— 1/8 个有
- `easy imageScaleDownToSize` —— 1/8 个有
- `easy positive` —— 1/8 个有

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
