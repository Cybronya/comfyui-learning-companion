---
name: unknown_workflow_lora_sampler_clip_27
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.716222
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ColorCorrect, Image Comparer (rgthree), ImageScaleBy, Int, KSampler, LoraLoaderModelOnly, MemoryCleaner, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-image2512+文生图+高清放大_2006552281617014786.json, 图片生成/文生图/Qwen-image2512文生图+seedvr2放大（4K）_2006688942132830209.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2006358896344047617.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2008143714165723138.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2011686421953781762.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2013576617548845058.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2061008676458156034.json, 图片生成/文生图/Qwen-image2512文生图_2007145074009837570.json, 图片生成/文生图/文生图-Qwen-image2512海报-字体-抽象-艺术摄影等_2007748442419896321.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Qwen-image2512+文生图+高清放大_2006552281617014786.json、图片生成/文生图/Qwen-image2512文生图+seedvr2放大（4K）_2006688942132830209.json、图片生成/文生图/Qwen-image2512文生图+高清放大_2006358896344047617.json、图片生成/文生图/Qwen-image2512文生图+高清放大_2008143714165723138.json、图片生成/文生图/Qwen-image2512文生图+高清放大_2011686421953781762.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ColorCorrect`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `Int`
- `KSampler`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `SeedVR2` —— 8/9 个有
- `SeedVR2BlockSwap` —— 8/9 个有
- `SeedVR2ExtraArgs` —— 8/9 个有
- `PreviewImage` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `CR Text` —— 3/9 个有
- `LoadImage` —— 2/9 个有
- `easy imageConcat` —— 2/9 个有
- `easy promptLine` —— 2/9 个有
- `easy seed` —— 2/9 个有
- `SeedVR2LoadDiTModel` —— 1/9 个有
- `SeedVR2LoadVAEModel` —— 1/9 个有
- `SeedVR2VideoUpscaler` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | res_2s | - | 9 | 100% |
| 调度器 | beta57 | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，9 个样本，一致性 100%
- 调度器 最常用 beta57，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
