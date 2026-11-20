---
name: unknown_workflow_lora_sampler_clip_84
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.923
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text Concatenate, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键优化滤镜+图片风格渲染_1903002764916727809.json, 图片生成/图生图/三分镜一致性掌控：轻松分开控制场景、人设与构图！_1921404322280587266.json, 图片生成/文生图/ComfyUI进阶教程：运用In-Context LoRA精准控制角色一致性_1920491097255251969.json, 图片生成/文生图/In-Context-Lora字体设计_2018938772628443138.json, 图片生成/文生图/【微电影】镜头风格一致性电影3分镜in-context微电影_1905062711074689026.json, 图片生成/文生图/一致性电影分镜头_In-Context-LoRA_1909546503734763521.json, 平台全量/一致性电影分镜头_In-Context-LoRA_1977364261645230082.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/一键优化滤镜+图片风格渲染_1903002764916727809.json、图片生成/图生图/三分镜一致性掌控：轻松分开控制场景、人设与构图！_1921404322280587266.json、图片生成/文生图/ComfyUI进阶教程：运用In-Context LoRA精准控制角色一致性_1920491097255251969.json、图片生成/文生图/In-Context-Lora字体设计_2018938772628443138.json、图片生成/文生图/【微电影】镜头风格一致性电影3分镜in-context微电影_1905062711074689026.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Concatenate (JPS)` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `Text Concatenate` —— 3/7 个有
- `Fast Bypasser (rgthree)` —— 2/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `ConditioningCombineMultiple+` —— 1/7 个有
- `ConditioningSetArea` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1984 | 7 | 69% |
| 高度 | 1536 | 1152 - 1536 | 7 | 89% |
| LoRA 模型强度 | 0.83 | 0.6 - 1 | 7 | 80% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1984，7 个样本
- 高度 中位数 1536，观测区间 1152 - 1536，7 个样本，取值集中（一致性 89%）
- LoRA 模型强度 中位数 0.83，观测区间 0.6 - 1，7 个样本，取值集中（一致性 80%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
