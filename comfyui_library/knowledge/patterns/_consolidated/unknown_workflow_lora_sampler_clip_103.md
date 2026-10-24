---
name: unknown_workflow_lora_sampler_clip_103
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8774
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, ColorCorrectOfUtils, ImageCASharpening+, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, RHHiddenNodes, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 写实美女（图生图）_1993170303243190274.json, 图片生成/图生图/【Wan2.2+Wan2.2图生图】去除塑料感（基础流）_1953315187753451522.json, 图片生成/图生图/【Wan2.2+Wan2.2图生图】真实感图像_1953394177310642177.json, 图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json, 图片生成/文生图/【wan2.2文生图V2】gemini3专业级人像摄影提示词_1991427455816790017.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_103

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Wan2.2 写实美女（图生图）_1993170303243190274.json、图片生成/图生图/【Wan2.2+Wan2.2图生图】去除塑料感（基础流）_1953315187753451522.json、图片生成/图生图/【Wan2.2+Wan2.2图生图】真实感图像_1953394177310642177.json、图片生成/文生图/【Wan2.2+Wan2.2文生图】去除塑料感（基础流）_1952858079282065409.json、图片生成/文生图/【wan2.2文生图V2】gemini3专业级人像摄影提示词_1991427455816790017.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorCorrectOfUtils`
- `ImageCASharpening+`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `RHHiddenNodes`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Seed` —— 4/5 个有
- `CR Text` —— 4/5 个有
- `FluxResolutionNode` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `VAEEncode` —— 3/5 个有
- `EmptyLatentImage` —— 2/5 个有
- `ImageResize+` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `RH_Prompter` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 16 | 16 - 16 | 5 | 100% |
| 采样算法 | 2 | 2 - 2 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | bong_tangent | - | 5 | 100% |
| 宽度 | 676 | - | 2 | 76% |
| 高度 | 864 | - | 2 | 59% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 16，观测区间 16 - 16，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，观测区间 2 - 2，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 bong_tangent，5 个样本，一致性 100%
- 宽度 中位数 676，样本不足，未给区间，2 个样本
- 高度 中位数 864，样本不足，未给区间，2 个样本
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
