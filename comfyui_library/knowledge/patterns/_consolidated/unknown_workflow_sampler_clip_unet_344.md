---
name: unknown_workflow_sampler_clip_unet_344
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.981333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux图生图标准版_在线生图_1892985856808927233.json, 图片生成/图生图/超强FLUX洗图神器FLUX.1_1906179257314234370.json, 图片生成/图生图/高质量洗图 -去除杂质、去油光、修复瑕疵_1914989945994342402.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_344

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux图生图标准版_在线生图_1892985856808927233.json、图片生成/图生图/超强FLUX洗图神器FLUX.1_1906179257314234370.json、图片生成/图生图/高质量洗图 -去除杂质、去油光、修复瑕疵_1914989945994342402.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Latent Batch Size` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `Bjornulf_ShowStringText` —— 1/3 个有
- `ImitationHueNode` —— 1/3 个有
- `Joy_caption` —— 1/3 个有
- `Joy_caption_load` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
