---
name: unknown_workflow_clip_unet_vae_3
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.9285
common_nodes: [CLIPLoader, CLIPTextEncode, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1978720948956319746.json, 视频生成/文生视频/1分钟生成一条视频，Wan2.2-Lightx2v，新版加速LoRA又更新！_1987367248606244865.json, 视频生成/文生视频/1949880459313463297.json, 视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2039513590809501698.json, 视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json, 视频生成/文生视频/UnifiedReward-Flex LoRA实测：Wan2.2动作逻辑与物理表现提升_2029085278756937729.json, 视频生成/文生视频/UnifiedReward-Flex LoRA：Wan2.2动作逻辑与物理表现升级_2029392351566766081.json, 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2042210649249423362.json, 视频生成/文生视频/1950186717304242177.json, 视频生成/文生视频/Wan2.2_文生视频4步LoRA加速-B站UP主@好奇漫步_1983147396660129793.json, 视频生成/文生视频/1949992424375500801.json, 视频生成/文生视频/1969656393957601281.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1978720948956319746.json、视频生成/文生视频/1分钟生成一条视频，Wan2.2-Lightx2v，新版加速LoRA又更新！_1987367248606244865.json、视频生成/文生视频/1949880459313463297.json、视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2039513590809501698.json、视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 11/12 个有
- `LoadImage` —— 10/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `WanImageToVideo` —— 8/12 个有
- `CreateVideo` —— 7/12 个有
- `SaveVideo` —— 7/12 个有
- `VHS_VideoCombine` —— 6/12 个有
- `EmptyHunyuanLatentVideo` —— 5/12 个有
- `PathchSageAttentionKJ` —— 4/12 个有
- `Label (rgthree)` —— 3/12 个有
- `ModelPatchTorchSettings` —— 2/12 个有
- `DWPreprocessor` —— 1/12 个有
- `FSamplerAdvanced` —— 1/12 个有
- `ImageConcanate` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有
- `Wan22FunControlToVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 64% |
| Prompt 约束强度(CFG) | 8 | 4 - 20 | 11 | 52% |
| 采样算法 | 1 | 1 - 3.5 | 11 | 37% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 64%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 20，11 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，11 个样本，取值分散，一致性仅 37%
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
