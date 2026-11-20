---
name: unknown_workflow_lora_sampler_clip_27
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.699692
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ColorCorrect, Image Comparer (rgthree), ImageScaleBy, Int, KSampler, LoraLoaderModelOnly, MemoryCleaner, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-image2512+文生图+高清放大_2006552281617014786.json, 图片生成/文生图/Qwen-image2512文生图+seedvr2放大（4K）_2006688942132830209.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2006358896344047617.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2008143714165723138.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2011686421953781762.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2013576617548845058.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2048380210885697538.json, 图片生成/文生图/Qwen-image2512文生图+高清放大_2061008676458156034.json, 图片生成/文生图/Qwen-image2512文生图_2007145074009837570.json, 图片生成/文生图/文生图-Qwen-image2512海报-字体-抽象-艺术摄影等_2007748442419896321.json, 平台全量/字体设计-Qwen-image2512_2009438376830705665.json, 平台全量/设计助手-你提要求-ai帮你做海报设计超好用_2008535403053195265.json, 平台全量/设计助手-你提需求-ai做设计-Qwen-image2512_2008515800465936386.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Qwen-image2512+文生图+高清放大_2006552281617014786.json、图片生成/文生图/Qwen-image2512文生图+seedvr2放大（4K）_2006688942132830209.json、图片生成/文生图/Qwen-image2512文生图+高清放大_2006358896344047617.json、图片生成/文生图/Qwen-image2512文生图+高清放大_2008143714165723138.json、图片生成/文生图/Qwen-image2512文生图+高清放大_2011686421953781762.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 13 个 workflow 都包含：
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
- `SeedVR2` —— 12/13 个有
- `SeedVR2BlockSwap` —— 12/13 个有
- `SeedVR2ExtraArgs` —— 12/13 个有
- `PreviewImage` —— 8/13 个有
- `Fast Groups Bypasser (rgthree)` —— 7/13 个有
- `CR Text` —— 6/13 个有
- `easy seed` —— 5/13 个有
- `LoadImage` —— 4/13 个有
- `RH_LLMAPI_NODE` —— 3/13 个有
- `ShowText|pysssss` —— 3/13 个有
- `easy imageConcat` —— 2/13 个有
- `easy promptLine` —— 2/13 个有
- `SeedVR2LoadDiTModel` —— 1/13 个有
- `SeedVR2LoadVAEModel` —— 1/13 个有
- `SeedVR2VideoUpscaler` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 13 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | res_2s | - | 13 | 100% |
| 调度器 | beta57 | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，13 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，13 个样本，一致性 100%
- 调度器 最常用 beta57，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（15/13 个样本）：Steps较低可能导致细节不足
