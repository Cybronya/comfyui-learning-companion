---
name: text_to_image_lora_sampler_clip_669
type: Text To Image
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConcatTextOfUtils, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima-aesthetic-1.1动漫、游戏人物直出+自定义提示词+各种lora文生图_2079217110898798593.json, 图片生成/文生图/anima 正式版文生图_2057111768463405058.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_669

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Anima-aesthetic-1.1动漫、游戏人物直出+自定义提示词+各种lora文生图_2079217110898798593.json、图片生成/文生图/anima 正式版文生图_2057111768463405058.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DapaoGeminiInstructionZhenzhenNode` —— 1/2 个有
- `FastGroupsBypassSwitch` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `孤海注释` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.75 | - | 2 | 95% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1560 | - | 2 | 77% |
| 高度 | 1440 | - | 2 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.75，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1560，样本不足，未给区间，2 个样本
- 高度 中位数 1440，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
