---
name: unknown_workflow_sampler_clip_vae_33
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.954143
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, VAELoader, WanImageToVideo]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/wan2.1量化_1920615619392110593.json, 视频生成/图生视频/wan2.1量化latent_1937276822209896450.json, 视频生成/图生视频/【老金驿站】Comfyui原生支持WAN2.1-i2v_1895293426588385281.json, 视频生成/图生视频/【老金驿站】高清WANi2v速度翻倍Magcache生成工作流_1934136795636355074.json, 视频生成/图生视频/官方版WAN 720P模型GGUF Q4加速图生视频工作流_1895515644396240897.json, 视频生成/图生视频/最新MagCache视频加速-图生视频_1933315168342581250.json, 视频生成/图生视频/极速抽卡版图生视频量化WAN，81帧2分25秒省流版！_1895517453516996610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_33

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/wan2.1量化_1920615619392110593.json、视频生成/图生视频/wan2.1量化latent_1937276822209896450.json、视频生成/图生视频/【老金驿站】Comfyui原生支持WAN2.1-i2v_1895293426588385281.json、视频生成/图生视频/【老金驿站】高清WANi2v速度翻倍Magcache生成工作流_1934136795636355074.json、视频生成/图生视频/官方版WAN 720P模型GGUF Q4加速图生视频工作流_1895515644396240897.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `VAELoader`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `UnetLoaderGGUF` —— 4/7 个有
- `UNETLoader` —— 3/7 个有
- `MagCache` —— 2/7 个有
- `ModelSamplingSD3` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SaveLatent` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 25 | 7 | 69% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | uni_pc | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 25，7 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
