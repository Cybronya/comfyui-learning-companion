---
name: unknown_workflow_clip_unet_vae
type: Unknown Workflow
frequency: 25
level: weak
coverage: 0.96164
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/二次元 紫藤萝花主题婚纱设计_2032027433515356161.json, 图片生成/文生图/全量版Z_IMAGE文生图工作流_2068260369071689729.json, 图片生成/文生图/关键帧生成_2069402773254397953.json, 图片生成/文生图/加速版文生图WAN2.2_1955257152644550657.json, 图片生成/文生图/千问大模型Z_Image 文生图大模型（目前最真实）_1994767919693410305.json, 图片生成/文生图/千问文生图工作流_1980117131083812865.json, 图片生成/文生图/原生z-image-turbo_2003323871308677121.json, 图片生成/文生图/快速文生图：Z-image_zimage_2019318395178586113.json, 图片生成/文生图/文生图  Z-image  zimage  超真实 去除AI味_2042796990563622914.json, 图片生成/文生图/文生图 Z-image  zimage 超真实_2042852589439553537.json, 图片生成/文生图/文生图 阿里 Z-image  超真实 去除AI味_2041885856356638722.json, 图片生成/文生图/文生图 阿里 Z-image  超真实 去除AI味_2042157391986298882.json, 图片生成/文生图/文生图++Z-image多图猫咪 真实感_2048956527746224129.json, 图片生成/文生图/文生图Qwen-Image-10步蒸馏_2018607735310393346.json, 图片生成/文生图/文生图_1999752689116475393.json, 图片生成/文生图/文生图_2018496192077897730.json, 图片生成/文生图/文生图超真实+去除AI味_2043505519566000130.json, 图片生成/文生图/文生图（新）_2007073715049205761.json, 图片生成/文生图/极速文生图_2044017764528033793.json, 图片生成/文生图/极速文生图_2044030659710160898.json, 图片生成/文生图/神里绫华  zimage_2014941793854427137.json, 图片生成/文生图/超真实文生图 Z-image  zimage   自然真实 没AI感_2046109081471029250.json, 图片生成/文生图/超真实文生图_2044746798295687169.json, 图片生成/文生图/雷电将军zimage 生成_2009993579749449730.json, 视频生成/图生视频/workflow-关键帧-Flux_2114650060762996737.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/二次元 紫藤萝花主题婚纱设计_2032027433515356161.json、图片生成/文生图/全量版Z_IMAGE文生图工作流_2068260369071689729.json、图片生成/文生图/关键帧生成_2069402773254397953.json、图片生成/文生图/加速版文生图WAN2.2_1955257152644550657.json、图片生成/文生图/千问大模型Z_Image 文生图大模型（目前最真实）_1994767919693410305.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 23/25 个有
- `VAEDecode` —— 23/25 个有
- `KSamplerAdvanced` —— 5/25 个有
- `CFGNorm` —— 3/25 个有
- `Lora Loader Stack (rgthree)` —— 3/25 个有
- `VAEDecodeTiled` —— 2/25 个有
- `PreviewImage` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 8 - 50 | 20 | 49% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 10 | 25 | 20% |
| 采样算法 | res_multistep | - | 25 | 64% |
| 调度器 | simple | - | 25 | 76% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/25 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 50，观测区间 8 - 50，20 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 10，25 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 res_multistep，25 个样本，一致性 64%
- 调度器 最常用 simple，25 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
