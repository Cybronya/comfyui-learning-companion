---
name: unknown_workflow_lora_sampler_clip_118
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9914
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageRangeFromBatch, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, Wan_video_prompt_generator, easy int]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1956141417343143938.json, 图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1957735710319112194.json, 图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1958426008351358977.json, 图片生成/文生图/Wan2.2文生图片 真实摄影  细腻皮肤质感_1960618336759480321.json, 图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1956141417343143938.json、图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1957735710319112194.json、图片生成/文生图/Wan2.2文生图·2K原生图像创作_写实摄影_1958426008351358977.json、图片生成/文生图/Wan2.2文生图片 真实摄影  细腻皮肤质感_1960618336759480321.json、图片生成/文生图/Wan2.2：文生图·2K原生高清，定义视觉新标准！图像创作_人像摄影_写实摄影_国风美女_1950418164367671297.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetImageRangeFromBatch`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `Wan_video_prompt_generator`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 14 | 14 - 14 | 5 | 100% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 14，观测区间 14 - 14，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
