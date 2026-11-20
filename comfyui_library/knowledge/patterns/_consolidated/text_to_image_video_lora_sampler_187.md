---
name: text_to_image_video_lora_sampler_187
type: Text To Image
frequency: 3
level: strong
coverage: 0.823667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, EmptyLatentImage, FastFilmGrain, FluxResolutionNode, JjkText, KSampler, LoraLoader, ModelSamplingSD3, PathchSageAttentionKJ, RH_Prompter, RH_Translator, SaveImage, ShowText, VAEDecode, VAELoader, WanVideoNAG]
problems: []
missing: []
members: [图片生成/文生图/Wan 2.1写实摄影文生图_1945372680700796929.json, 图片生成/文生图/【降维打击】Wan2.1 文生图｜高质量图像_1947532482343243777.json, 平台全量/写实摄影Wan 2.1 txt2img_1943608894898008065.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_187

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Wan 2.1写实摄影文生图_1945372680700796929.json、图片生成/文生图/【降维打击】Wan2.1 文生图｜高质量图像_1947532482343243777.json、平台全量/写实摄影Wan 2.1 txt2img_1943608894898008065.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `FastFilmGrain`
- `FluxResolutionNode`
- `JjkText`
- `KSampler`
- `LoraLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RH_Prompter`
- `RH_Translator`
- `SaveImage`
- `ShowText`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 2/3 个有
- `TextCombinerSix` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1280 | 1280 - 1280 | 3 | 100% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
