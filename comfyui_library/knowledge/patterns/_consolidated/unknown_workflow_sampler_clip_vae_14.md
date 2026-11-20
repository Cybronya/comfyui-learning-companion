---
name: unknown_workflow_sampler_clip_vae_14
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.989071
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, SaveVideo, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-Lightx2v latest_1988041568177295362.json, 视频生成/图生视频/Wan2.2-Lightx2v-1108新版加速LoRA_1988138088604004353.json, 视频生成/图生视频/Wan2.2-live2D-动态壁纸制造机_1982368438184230913.json, 视频生成/图生视频/Wan2.2-live2D-动态壁纸即刻实现_2044955303057301505.json, 视频生成/图生视频/Wan2.2-live2D-动态壁纸生成_2049008127445573634.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸_2079750552161968129.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成_2077588507496894466.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成_2079019127112556545.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成_2079108169829273601.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成：可爱兔子吃夹饼_2082362157714460674.json, 视频生成/图生视频/Wan2.2-live2D动态壁纸一键生成：旷野兔动态壁纸工作流_2082287620427706369.json, 视频生成/图生视频/Wan2.2-live2d高级可定制版-动态壁纸--可定制尺寸及时长-24fps版_2064561200037457922.json, 视频生成/图生视频/Wan2.2_14B_图生视频-加速版-KJ模型_1950521447607357441.json, 视频生成/图生视频/wan2.2_14B_VACE_GGUF_图生视频-加速版_1950557926740119553.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_14

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-Lightx2v latest_1988041568177295362.json、视频生成/图生视频/Wan2.2-Lightx2v-1108新版加速LoRA_1988138088604004353.json、视频生成/图生视频/Wan2.2-live2D-动态壁纸制造机_1982368438184230913.json、视频生成/图生视频/Wan2.2-live2D-动态壁纸即刻实现_2044955303057301505.json、视频生成/图生视频/Wan2.2-live2D-动态壁纸生成_2049008127445573634.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `SaveVideo`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 13/14 个有
- `ModelSamplingSD3` —— 13/14 个有
- `UNETLoader` —— 13/14 个有
- `WanImageToVideo` —— 13/14 个有
- `PathchSageAttentionKJ` —— 12/14 个有
- `CFGZeroStar` —— 10/14 个有
- `ImpactInt` —— 2/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/14 个有
- `SimpleMath+` —— 2/14 个有
- `Text` —— 2/14 个有
- `TrimVideoLatent` —— 1/14 个有
- `UnetLoaderGGUF` —— 1/14 个有
- `WanVaceToVideo` —— 1/14 个有
- `workflow>LORA1` —— 1/14 个有
- `workflow>LORA2` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 14 | 100% |
| Prompt 约束强度(CFG) | 20 | 6 - 20 | 14 | 70% |
| 采样算法 | 3.5 | 1 - 3.5 | 14 | 65% |
| 调度器 | euler | - | 14 | 100% |
| 重绘幅度 | simple | - | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，14 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 6 - 20，14 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，14 个样本
- 调度器 最常用 euler，14 个样本，一致性 100%
- 重绘幅度 最常用 simple，14 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
