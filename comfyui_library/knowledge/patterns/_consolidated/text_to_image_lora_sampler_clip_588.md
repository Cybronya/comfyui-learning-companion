---
name: text_to_image_lora_sampler_clip_588
type: Text To Image
frequency: 3
level: strong
coverage: 0.852
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, FastFilmGrain, KSampler, LayerColor: BrightnessContrastV2, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/一键生成自媒体封面V2_2036289953994383361.json, 图片生成/文生图/自媒体封面设计平面海报设计 RH工作流+应用封面生成_2044600478033518593.json, 平台全量/Z-Image-瑶光版-超真实细节增强_2119058420929220609.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_588

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/一键生成自媒体封面V2_2036289953994383361.json、图片生成/文生图/自媒体封面设计平面海报设计 RH工作流+应用封面生成_2044600478033518593.json、平台全量/Z-Image-瑶光版-超真实细节增强_2119058420929220609.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `FastFilmGrain`
- `KSampler`
- `LayerColor: BrightnessContrastV2`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `StringFunction|pysssss` —— 2/3 个有
- `Text` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s | - | 3 | 100% |
| 调度器 | bong_tangent | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 920 | 920 - 1080 | 3 | 92% |
| 高度 | 1280 | 1280 - 1920 | 3 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，3 个样本，一致性 100%
- 调度器 最常用 bong_tangent，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 920，观测区间 920 - 1080，3 个样本，取值集中（一致性 92%）
- 高度 中位数 1280，观测区间 1280 - 1920，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
