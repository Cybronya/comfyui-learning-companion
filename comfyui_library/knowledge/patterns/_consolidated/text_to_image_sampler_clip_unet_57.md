---
name: text_to_image_sampler_clip_unet_57
type: Text To Image
frequency: 8
level: weak
coverage: 0.829625
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Ernie对比工作流_2048756036944797698.json, 图片生成/文生图/Krea2 Instagram 摄影风格文生图_2087916354635649025.json, 图片生成/文生图/Krea2 Turbo 单色水墨风格文生图_2078458901254725633.json, 图片生成/文生图/Krea2 Turbo 柔和极简素描风格文生图_2078480779449032705.json, 图片生成/文生图/Krea2 Turbo 真实感写实风格文生图_2078379281394257921.json, 图片生成/文生图/Krea2 Turbo 空灵闪耀光风格文生图_2078478130687336450.json, 图片生成/文生图/Krea2 Turbo 青绿色水彩插画风格文生图_2078398716591042562.json, 图片生成/文生图/realism_engine_krea2（自动扩写提示词）_2072599087316299777.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_57

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Ernie对比工作流_2048756036944797698.json、图片生成/文生图/Krea2 Instagram 摄影风格文生图_2087916354635649025.json、图片生成/文生图/Krea2 Turbo 单色水墨风格文生图_2078458901254725633.json、图片生成/文生图/Krea2 Turbo 柔和极简素描风格文生图_2078480779449032705.json、图片生成/文生图/Krea2 Turbo 真实感写实风格文生图_2078379281394257921.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `StringConcatenate` —— 7/8 个有
- `EmptyFlux2LatentImage` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `StringReplace` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 8 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 28% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1920 | 8 | 74% |
| 高度 | 1024 | 1024 - 1080 | 8 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，8 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1920，8 个样本
- 高度 中位数 1024，观测区间 1024 - 1080，8 个样本，取值集中（一致性 98%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
