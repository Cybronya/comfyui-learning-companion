---
name: text_to_image_sampler_clip_unet_99
type: Text To Image
frequency: 4
level: weak
coverage: 0.87575
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima V1.1 文生图_2078367758005399554.json, 图片生成/文生图/Krea2 Turbo风格迁移（双采反推版）_2070490329257697282.json, 图片生成/文生图/超自然文生美女_2075426810342502402.json, 视频生成/图生视频/Krea-人物素材_2089973989698523138.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_99

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Anima V1.1 文生图_2078367758005399554.json、图片生成/文生图/Krea2 Turbo风格迁移（双采反推版）_2070490329257697282.json、图片生成/文生图/超自然文生美女_2075426810342502402.json、视频生成/图生视频/Krea-人物素材_2089973989698523138.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `ConcatTextOfUtils` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `JoinStrings` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `Random Line` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 4 | 98% |
| 高度 | 1280 | 1024 - 1920 | 4 | 73% |
| 采样步数 | 9 | 6 - 40 | 4 | 13% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 4 | 19% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 0.4 - 1 | 4 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，4 个样本，取值集中（一致性 98%）
- 高度 中位数 1280，观测区间 1024 - 1920，4 个样本
- 采样步数 中位数 9，观测区间 6 - 40，4 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，4 个样本
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
