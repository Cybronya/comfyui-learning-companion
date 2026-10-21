---
name: text_to_image_sampler_clip_unet_44
type: Text To Image
frequency: 10
level: weak
coverage: 0.9779
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/boogu Turbo Hotfix修复版极速文生图_2072876509190254594.json, 图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2073336372441739265.json, 图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2073991622328668161.json, 图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2074374671864258562.json, 图片生成/文生图/boogu文生图满血版工作流_2067862555661520898.json, 图片生成/文生图/boogu文生图满血版工作流_2067880773423816705.json, 图片生成/文生图/boogu满血版文生图V1_2067838674468958210.json, 图片生成/文生图/boogu满血版文生图V1_2068275477441236993.json, 图片生成/文生图/krea 2 文生图工作流_2079525843776393218.json, 图片生成/文生图/（贞贞lora）z-image-turbo flow dpo版文生图V1_2026975683213266946.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_44

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/boogu Turbo Hotfix修复版极速文生图_2072876509190254594.json、图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2073336372441739265.json、图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2073991622328668161.json、图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2074374671864258562.json、图片生成/文生图/boogu文生图满血版工作流_2067862555661520898.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 9/10 个有
- `ResolutionSelector` —— 5/10 个有
- `easy seed` —— 5/10 个有
- `PreviewAny` —— 4/10 个有
- `QwenImageEngineer` —— 4/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `RTXVideoSuperResolution` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1920 | 10 | 69% |
| 高度 | 1024 | 512 - 1536 | 10 | 78% |
| 采样步数 | 9 | 4 - 50 | 10 | 7% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 33% |
| 采样算法 | ddim | - | 10 | 80% |
| 调度器 | beta57 | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1920，10 个样本
- 高度 中位数 1024，观测区间 512 - 1536，10 个样本
- 采样步数 中位数 9，观测区间 4 - 50，10 个样本，取值分散，一致性仅 7%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 ddim，10 个样本，一致性 80%
- 调度器 最常用 beta57，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（8/10 个样本）：Steps较低可能导致细节不足
