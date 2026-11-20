---
name: unknown_workflow_lora_sampler_clip_110
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.906
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ImageBatchMulti, KSampler, LoraLoader, ModelSamplingAuraFlow, PreviewAny, RunningHub_ZImageI2L_Loader, RunningHub_ZImageI2L_LoraGenerator, RunningHub_ZImageI2L_Saver, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Z-image  I2L 风格 lora 训练_2079502114396659713.json, 图片生成/图生图/Z-image Base I2L 风格lora训练+生图集成版V1_2016591920394407938.json, 图片生成/图生图/（多图推荐）风格lora，游戏_动漫角色设计_2055482972308025346.json, 图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+测试_2023308170269036545.json, 平台全量/Z-image Base I2L 风格 lora 训练，一秒生成_2016860029290291202.json, 平台全量/快速训练风格lora-可下载-Z-image Base I2L_2018617913829232641.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_110

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-image  I2L 风格 lora 训练_2079502114396659713.json、图片生成/图生图/Z-image Base I2L 风格lora训练+生图集成版V1_2016591920394407938.json、图片生成/图生图/（多图推荐）风格lora，游戏_动漫角色设计_2055482972308025346.json、图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+测试_2023308170269036545.json、平台全量/Z-image Base I2L 风格 lora 训练，一秒生成_2016860029290291202.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ImageBatchMulti`
- `KSampler`
- `LoraLoader`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `RunningHub_ZImageI2L_Loader`
- `RunningHub_ZImageI2L_LoraGenerator`
- `RunningHub_ZImageI2L_Saver`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `Anything Everywhere` —— 1/6 个有
- `FeishuConfigNode` —— 1/6 个有
- `FeishuFetchImageNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 28 - 50 | 6 | 82% |
| Prompt 约束强度(CFG) | 4 | 2.5 - 4 | 6 | 85% |
| 采样算法 | res_multistep | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | 1 - 1.1 | 6 | 96% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 28 - 50，6 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 2.5 - 4，6 个样本，取值集中（一致性 85%）
- 采样算法 最常用 res_multistep，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1.1，6 个样本，取值集中（一致性 96%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
