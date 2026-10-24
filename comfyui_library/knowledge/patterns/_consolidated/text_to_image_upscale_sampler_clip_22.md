---
name: text_to_image_upscale_sampler_clip_22
type: Text To Image
frequency: 5
level: strong
coverage: 0.8024
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima3—动漫图像模型+ 自动提示词扩写_2049482150319230977.json, 图片生成/文生图/Anima3—动漫图像模型全自动进化模式_2049003395775729665.json, 图片生成/文生图/Anima3动漫_反推提示词+全自动进化模式_2049394805997834242.json, 图片生成/文生图/Anima预览版动漫模型-文生图 邪修版 RH工作流_2021210100874092545.json, 图片生成/文生图/全新Anima3动漫图像模型-文生图-高级工作流_2049713795706175490.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Anima3—动漫图像模型+ 自动提示词扩写_2049482150319230977.json、图片生成/文生图/Anima3—动漫图像模型全自动进化模式_2049003395775729665.json、图片生成/文生图/Anima3动漫_反推提示词+全自动进化模式_2049394805997834242.json、图片生成/文生图/Anima预览版动漫模型-文生图 邪修版 RH工作流_2021210100874092545.json、图片生成/文生图/全新Anima3动漫图像模型-文生图-高级工作流_2049713795706175490.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `RH_LLMAPI_Pro_Node` —— 4/5 个有
- `DuckHideNode` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 768 - 1080 | 5 | 89% |
| 高度 | 1152 | 1024 - 1920 | 5 | 75% |
| 采样步数 | 40 | 30 - 40 | 5 | 89% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 80% |
| 调度器 | beta57 | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 768 - 1080，5 个样本，取值集中（一致性 89%）
- 高度 中位数 1152，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 40，观测区间 30 - 40，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 80%
- 调度器 最常用 beta57，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
