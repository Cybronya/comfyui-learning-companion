---
name: unknown_workflow_clip_unet_vae_2
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.899417
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy cleanGpuUsed, easy clearCacheAll]
members: [图片生成/文生图/1944626515541676033.json, 图片生成/文生图/1950183203102441473.json, 图片生成/文生图/1950184764194119681.json, 图片生成/文生图/1950527410125066242.json, 图片生成/文生图/1950935703578419201.json, 图片生成/文生图/1951146831617175554.json, 图片生成/文生图/1951193822992773122.json, 图片生成/文生图/1951482093362688001.json, 图片生成/文生图/1951900115835498497.json, 图片生成/文生图/1954740605987504129.json, 图片生成/文生图/1960284703142129666.json, 图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1944626515541676033.json、图片生成/文生图/1950183203102441473.json、图片生成/文生图/1950184764194119681.json、图片生成/文生图/1950527410125066242.json、图片生成/文生图/1950935703578419201.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/12 个有
- `ModelSamplingSD3` —— 8/12 个有
- `easy cleanGpuUsed` —— 7/12 个有
- `KSampler` —— 6/12 个有
- `KSamplerAdvanced` —— 6/12 个有
- `FastFilmGrain` —— 3/12 个有
- `Int` —— 3/12 个有
- `LoraLoader` —— 3/12 个有
- `WanVideoNAG` —— 3/12 个有
- `easy clearCacheAll` —— 3/12 个有
- `LoadImage` —— 2/12 个有
- `SaveAnimatedWEBP` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 11 | 10 - 20 | 6 | 67% |
| Prompt 约束强度(CFG) | 5.75 | 1 - 20 | 12 | 5% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 36% |
| 调度器 | beta | - | 12 | 33% |
| 重绘幅度 | 1 | 0.3 - 1 | 6 | 70% |
| LoRA 模型强度 | 1 | 0.6 - 1 | 3 | 78% |
| LoRA 文本强度 | 1 | 0.6 - 1 | 3 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 11，观测区间 10 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 5.75，观测区间 1 - 20，12 个样本，取值分散，一致性仅 5%
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 36%
- 调度器 最常用 beta，12 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，6 个样本
- LoRA 模型强度 中位数 1，观测区间 0.6 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 0.6 - 1，3 个样本
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、easy clearCacheAll
