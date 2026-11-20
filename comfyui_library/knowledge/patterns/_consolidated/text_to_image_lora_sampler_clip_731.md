---
name: text_to_image_lora_sampler_clip_731
type: Text To Image
frequency: 2
level: weak
coverage: 0.932
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), JoinStrings, KSampler, LoadImage, PreviewImage, ProcessString, Prompt_Text, ResolutionMaster, SaveImage, UNETLoader, VAEDecode, VAELoader, easy loraStack, easy loraStackApply, easy promptLine, easy seed]
problems: []
missing: []
members: [图片生成/文生图/🦊Krea2-文生图多主模+多lora整合版_2116456467418140674.json, 图片生成/文生图/🦊Krea2-文生图多主模+多lora整合版_2116680112216297473.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_731

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/🦊Krea2-文生图多主模+多lora整合版_2116456467418140674.json、图片生成/文生图/🦊Krea2-文生图多主模+多lora整合版_2116680112216297473.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JoinStrings`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ProcessString`
- `Prompt_Text`
- `ResolutionMaster`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy loraStack`
- `easy loraStackApply`
- `easy promptLine`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1344 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1344，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
