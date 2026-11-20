---
name: text_to_image_sampler_clip_unet_108
type: Text To Image
frequency: 7
level: weak
coverage: 0.868714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima V1.1 文生图_2078367758005399554.json, 图片生成/文生图/Qwen 3.5 反推图片提示词_2063823684560834561.json, 图片生成/文生图/krea2田园风格MJ感工作流_2102923019374125057.json, 图片生成/文生图/krea2田园风格MJ感工作流_2104384123690373122.json, 图片生成/文生图/krea2田园风格MJ感工作流_2104754840189624322.json, 平台全量/Qwen 3.5 反推图片提示词_2117210456434761729.json, 平台全量/krea2 田园风格MJ感工作流_2119834203008356354.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_108

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Anima V1.1 文生图_2078367758005399554.json、图片生成/文生图/Qwen 3.5 反推图片提示词_2063823684560834561.json、图片生成/文生图/krea2田园风格MJ感工作流_2102923019374125057.json、图片生成/文生图/krea2田园风格MJ感工作流_2104384123690373122.json、图片生成/文生图/krea2田园风格MJ感工作流_2104754840189624322.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `CR Prompt Text` —— 5/7 个有
- `ConditioningKrea2Rebalance` —— 4/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `PreviewAny` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `TTResolutionSelector` —— 4/7 个有
- `LoadImage` —— 2/7 个有
- `ConcatTextOfUtils` —— 1/7 个有
- `Random Line` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 7 | 97% |
| 高度 | 1024 | 1024 - 1920 | 7 | 69% |
| 采样步数 | 8 | 8 - 40 | 7 | 11% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 7 | 18% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，7 个样本，取值集中（一致性 97%）
- 高度 中位数 1024，观测区间 1024 - 1920，7 个样本
- 采样步数 中位数 8，观测区间 8 - 40，7 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
