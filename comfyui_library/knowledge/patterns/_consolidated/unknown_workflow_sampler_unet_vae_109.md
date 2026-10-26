---
name: unknown_workflow_sampler_unet_vae_109
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.858667
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1_三视图+多表情+多视角_2109917911023439874.json, 图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json, 图片生成/图生图/Qwen Image 2.1去除ai感_2102264547909390337.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2107745252730826754.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2108519033753653250.json, 图片生成/图生图/Qwen Image 2.1多图编辑！B站艾橘溪_2102245556734218241.json, 图片生成/图生图/双人场景合成丨Qwen Image 2.1丨三图融合·提示词增强_2112093043179479041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_109

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1_三视图+多表情+多视角_2109917911023439874.json、图片生成/图生图/Qwen Image 2.1单图编辑（角色四视图）2609_2106315774649528321.json、图片生成/图生图/Qwen Image 2.1去除ai感_2102264547909390337.json、图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json、图片生成/图生图/Qwen Image 2.1多图编辑_2102401818163765249.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 8/9 个有
- `QwenImage21Cache` —— 8/9 个有
- `JjkText` —— 7/9 个有
- `BatchImagesNode` —— 6/9 个有
- `TextGenerateLTX2Prompt` —— 5/9 个有
- `easy imageConcat` —— 3/9 个有
- `ImageStitch` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `CompressImages` —— 1/9 个有
- `ImageScale` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `TextGenerate` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 9 | 98% |
| 高度 | 1024 | 1024 - 1920 | 9 | 75% |
| 采样步数 | 50 | 25 - 50 | 9 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，9 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，9 个样本
- 采样步数 中位数 50，观测区间 25 - 50，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
