---
name: text_to_image_upscale_latent_upscale_lora_13
type: Text To Image
frequency: 3
level: weak
coverage: 0.854333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize+, INTConstant, KSampler, LatentUpscaleBy, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, SaveImage, SimpleMathDual+, TTResolutionSelector, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/K2双采文生图批量出图 自动SD放大风格强化开源追MJ_2104761502413713409.json, 图片生成/文生图/【K2-双采V2】图生图_洗图专用_可批量_自动2K放大_风格强化_2104659775685488641.json, 图片生成/文生图/【K2-双采】文生图_可批量_自动SD放大_风格强化_开源也想追上MJ！_2104243273622708225.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/K2双采文生图批量出图 自动SD放大风格强化开源追MJ_2104761502413713409.json、图片生成/文生图/【K2-双采V2】图生图_洗图专用_可批量_自动2K放大_风格强化_2104659775685488641.json、图片生成/文生图/【K2-双采】文生图_可批量_自动SD放大_风格强化_开源也想追上MJ！_2104243273622708225.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize+`
- `INTConstant`
- `KSampler`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `SimpleMathDual+`
- `TTResolutionSelector`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MemoryCleaner` —— 2/3 个有
- `ImageSmartSharpen+` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `easy positive` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 11 | 3 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.58 - 1 | 3 | 77% |
| 宽度 | 1024 | 80 - 1024 | 3 | 37% |
| 高度 | 1024 | 80 - 1024 | 3 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 11，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.58 - 1，3 个样本
- 宽度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
- 高发问题（2/3 个样本）：发现KSampler但没有VAEDecode
