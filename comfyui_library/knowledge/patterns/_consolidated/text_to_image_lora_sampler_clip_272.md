---
name: text_to_image_lora_sampler_clip_272
type: Text To Image
frequency: 7
level: strong
coverage: 0.916714
common_nodes: [CLIPLoaderGGUF, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DF_Float, EmptyLatentImage, Int, KSampler, LoraLoaderModelOnly, SaveImage, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/文生图/zimage dnd风格半写实奇幻数字插画工作流_2076506450293252098.json, 图片生成/文生图/zimage 最新光影lora+提示词_2074663614140731394.json, 图片生成/文生图/zimage 最新光影lora+提示词_2074689079039578114.json, 图片生成/文生图/zimage 最新光影lora+提示词_2075146341201825794.json, 图片生成/文生图/zimage 最新光影lora+提示词_2076916021839089665.json, 图片生成/文生图/zimage 最新光影lora+提示词_2078001416542711809.json, 图片生成/文生图/zimage 最新光影lora+提示词工程师，让强的更强！_2028076084645863425.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_272

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/zimage dnd风格半写实奇幻数字插画工作流_2076506450293252098.json、图片生成/文生图/zimage 最新光影lora+提示词_2074663614140731394.json、图片生成/文生图/zimage 最新光影lora+提示词_2074689079039578114.json、图片生成/文生图/zimage 最新光影lora+提示词_2075146341201825794.json、图片生成/文生图/zimage 最新光影lora+提示词_2076916021839089665.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DF_Float`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 1/7 个有
- `JjkText` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1920 - 1920 | 7 | 100% |
| 高度 | 1080 | 1080 - 1080 | 7 | 100% |
| 采样步数 | 10 | 10 - 10 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1920，观测区间 1920 - 1920，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，观测区间 1080 - 1080，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
