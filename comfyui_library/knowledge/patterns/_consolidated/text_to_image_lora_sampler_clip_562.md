---
name: text_to_image_lora_sampler_clip_562
type: Text To Image
frequency: 3
level: strong
coverage: 0.855667
common_nodes: [CLIPLoaderGGUF, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, easy int]
problems: []
missing: []
members: [图片生成/文生图/ZIT_v20.safetensors，小日子模型升级版_2058925000341671937.json, 图片生成/文生图/ZIT_v30.safetensors_2072566206896365569.json, 图片生成/文生图/ZITuwazumimixZIT_v20.safetensors，小日子模型_2047232881449246722.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_562

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/ZIT_v20.safetensors，小日子模型升级版_2058925000341671937.json、图片生成/文生图/ZIT_v30.safetensors_2072566206896365569.json、图片生成/文生图/ZITuwazumimixZIT_v20.safetensors，小日子模型_2047232881449246722.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `DeepTranslatorTextNode` —— 2/3 个有
- `ProcessString` —— 2/3 个有
- `LoadImage` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 30 | 10 - 30 | 3 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 10 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
