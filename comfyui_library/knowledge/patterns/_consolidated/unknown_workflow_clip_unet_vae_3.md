---
name: unknown_workflow_clip_unet_vae_3
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.949353
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/二次元 紫藤萝花主题婚纱设计_2032027433515356161.json, 图片生成/文生图/快速文生图：Z-image_zimage_2019318395178586113.json, 图片生成/文生图/文生图  Z-image  zimage  超真实 去除AI味_2042796990563622914.json, 图片生成/文生图/文生图 Z-image  zimage 超真实_2042852589439553537.json, 图片生成/文生图/文生图 阿里 Z-image  超真实 去除AI味_2041885856356638722.json, 图片生成/文生图/文生图 阿里 Z-image  超真实 去除AI味_2042157391986298882.json, 图片生成/文生图/文生图-极致自然-Z-Image-Base_2016417634937475073.json, 图片生成/文生图/文生图Qwen-Image-10步蒸馏_2018607735310393346.json, 图片生成/文生图/文生图_1999752689116475393.json, 图片生成/文生图/文生图_2018496192077897730.json, 图片生成/文生图/文生图（新）_2007073715049205761.json, 图片生成/文生图/极速文生图_2044017764528033793.json, 图片生成/文生图/极速文生图_2044030659710160898.json, 图片生成/文生图/海报生成器+QwenImage=艾橘溪_1954567812612288513.json, 图片生成/文生图/神里绫华  zimage_2014941793854427137.json, 图片生成/文生图/艺术字体生成器+QwenImage=B站艾橘溪_1954565922696654850.json, 图片生成/文生图/雷电将军zimage 生成_2009993579749449730.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/二次元 紫藤萝花主题婚纱设计_2032027433515356161.json、图片生成/文生图/快速文生图：Z-image_zimage_2019318395178586113.json、图片生成/文生图/文生图  Z-image  zimage  超真实 去除AI味_2042796990563622914.json、图片生成/文生图/文生图 Z-image  zimage 超真实_2042852589439553537.json、图片生成/文生图/文生图 阿里 Z-image  超真实 去除AI味_2041885856356638722.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 15/17 个有
- `VAEDecode` —— 15/17 个有
- `KSamplerAdvanced` —— 5/17 个有
- `CFGNorm` —— 3/17 个有
- `Lora Loader Stack (rgthree)` —— 3/17 个有
- `easy cleanGpuUsed` —— 3/17 个有
- `VAEDecodeTiled` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 10 - 50 | 12 | 65% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 10 | 17 | 36% |
| 采样算法 | res_multistep | - | 17 | 59% |
| 调度器 | simple | - | 17 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/17 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 50，观测区间 10 - 50，12 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 10，17 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 res_multistep，17 个样本，一致性 59%
- 调度器 最常用 simple，17 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
