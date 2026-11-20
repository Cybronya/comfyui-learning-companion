---
name: text_to_image_lora_sampler_clip_356
type: Text To Image
frequency: 6
level: strong
coverage: 0.7795
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/超自然文生美女_2075426810342502402.json, 图片生成/文生图/（Zhen style风格模型）Krea2 Turbo文生图V1_2071136461566599169.json, 图片生成/文生图/（图图版）Krea2 Turbo文生图V1_2072524020372828162.json, 图片生成/文生图/（贞贞版-Raw Lora 1000步）Krea2 Turbo文生图V1_2073809636901351425.json, 图片生成/文生图/（贞贞版）Krea2 Turbo文生图V1_2070539771801325570.json, 视频生成/图生视频/Krea-人物素材_2089973989698523138.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_356

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/超自然文生美女_2075426810342502402.json、图片生成/文生图/（Zhen style风格模型）Krea2 Turbo文生图V1_2071136461566599169.json、图片生成/文生图/（图图版）Krea2 Turbo文生图V1_2072524020372828162.json、图片生成/文生图/（贞贞版-Raw Lora 1000步）Krea2 Turbo文生图V1_2073809636901351425.json、图片生成/文生图/（贞贞版）Krea2 Turbo文生图V1_2070539771801325570.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `StringConcatenate` —— 5/6 个有
- `TextConcat` —— 4/6 个有
- `TextGenerate` —— 4/6 个有
- `llama_cpp_instruct_adv` —— 2/6 个有
- `llama_cpp_model_loader` —— 2/6 个有
- `llama_cpp_parameters` —— 2/6 个有
- `INTConstant` —— 1/6 个有
- `JoinStrings` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 6 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1536 | 6 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，6 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，6 个样本，取值集中（一致性 83%）
