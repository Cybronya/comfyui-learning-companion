---
name: text_to_image_lora_sampler_clip_725
type: Text To Image
frequency: 2
level: weak
coverage: 0.842
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, CR Text Concatenate, DF_Text_Box, DualCLIPLoader, EmptyLatentImage, ImpactSwitch, KSampler, LoadImage, LoraLoader, RH_Captioner, RH_Translator, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/沙雕人物专用工作流_2075022505315749889.json, 图片生成/文生图/沙雕动画人物生成_动画制作专用_2011123524311715841.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_725

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/沙雕人物专用工作流_2075022505315749889.json、图片生成/文生图/沙雕动画人物生成_动画制作专用_2011123524311715841.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Text Concatenate`
- `DF_Text_Box`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ImpactSwitch`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `RH_Captioner`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 720 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
