---
name: text_to_image_video_lora_sampler_84
type: Text To Image
frequency: 9
level: strong
coverage: 0.888556
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Unified, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/全能插件加速版minimaxH3数字人工作流_2087430084268482561.json, 视频生成/图生视频/商业级360度环绕镜头展示｜产品级运镜一镜到底_2111325834421293058.json, 视频生成/文生视频/8步768p加速新版 MiniMax H3 单采高质量文生视频_2094171689625153537.json, 视频生成/文生视频/8步768p加速新版｜MiniMax H3单采高质量三模视频_2094310836981551107.json, 视频生成/文生视频/Minimax双采全功能视频工作流｜文生视频图生视频视频生视频三合一_2088696202564038657.json, 视频生成/文生视频/全功能双采二选一｜Minimax文生视频图生视频视频生视频_2089019399863889922.json, 视频生成/文生视频/单采高质量加速版｜MiniMax H3去除人物油腻处理_2092550530987020289.json, 视频生成/文生视频/电影感画面增强｜MiniMax H3文生图生视频处理_2093220651229335554.json, 视频生成/文生视频/电影感画面增强｜MiniMax H3文生视频视频重绘_2093065468214071297.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/全能插件加速版minimaxH3数字人工作流_2087430084268482561.json、视频生成/图生视频/商业级360度环绕镜头展示｜产品级运镜一镜到底_2111325834421293058.json、视频生成/文生视频/8步768p加速新版 MiniMax H3 单采高质量文生视频_2094171689625153537.json、视频生成/文生视频/8步768p加速新版｜MiniMax H3单采高质量三模视频_2094310836981551107.json、视频生成/文生视频/Minimax双采全功能视频工作流｜文生视频图生视频视频生视频三合一_2088696202564038657.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

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
- `LoraLoaderModelOnly`
- `MiniMaxH3Unified`
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `ModelAttentionBackend` —— 8/9 个有
- `ModelPreviewOverrideKJ` —— 6/9 个有
- `VAEDecodeAudio` —— 6/9 个有
- `MiniMaxH3SigmaShift` —— 5/9 个有
- `PrimitiveFloat` —— 5/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `CR Text` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `MiniMaxH3AVDecodeT8` —— 3/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `PT_H3ConcatAVLatent` —— 2/9 个有
- `VAEEncode` —— 2/9 个有
- `easy clearCacheAll` —— 2/9 个有
- `LoadImage` —— 1/9 个有
- `MemoryCleaner` —— 1/9 个有
- `MiniMaxChunkFeedForward` —— 1/9 个有
- `MiniMaxLowVRAMAttention` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/9 个有

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
