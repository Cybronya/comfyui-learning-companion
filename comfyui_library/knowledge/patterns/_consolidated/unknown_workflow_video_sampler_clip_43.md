---
name: unknown_workflow_video_sampler_clip_43
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.941917
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/空白工作流_2023806370599931905.json, 视频生成/图生视频/视频用这个_2023300078865223682.json, 视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频_1949880459313463297.json, 视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2039513590809501698.json, 视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json, 视频生成/文生视频/ComfyUI官方图生视频工作流搭建_2050410359365881858.json, 视频生成/文生视频/Remix_i2v_v2.1工作流_2050521770255495170.json, 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_1949440813809467394.json, 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2018552915408982018.json, 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2042210649249423362.json, 视频生成/文生视频/WAN2.2 文生视频女孩穿梭_1950186717304242177.json, 视频生成/文生视频/Wan2.2&lightx2v加速_1950385703961149441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/空白工作流_2023806370599931905.json、视频生成/图生视频/视频用这个_2023300078865223682.json、视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频_1949880459313463297.json、视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2039513590809501698.json、视频生成/文生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2044307342530977793.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/12 个有
- `EmptyHunyuanLatentVideo` —— 7/12 个有
- `PathchSageAttentionKJ` —— 5/12 个有
- `ModelPatchTorchSettings` —— 3/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `LoadVideo` —— 2/12 个有
- `CFGZeroStarAndInit` —— 1/12 个有
- `WanVideoEnhanceAVideoKJ` —— 1/12 个有
- `WanVideoSampler` —— 1/12 个有
- `WanVideoTeaCache` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 58% |
| Prompt 约束强度(CFG) | 8 | 4 - 14 | 12 | 60% |
| 采样算法 | 1.05 | 1 - 3.5 | 12 | 37% |
| 调度器 | euler | - | 12 | 92% |
| 重绘幅度 | simple | - | 12 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 58%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 14，12 个样本
- 采样算法 中位数 1.05，观测区间 1 - 3.5，12 个样本，取值分散，一致性仅 37%
- 调度器 最常用 euler，12 个样本，一致性 92%
- 重绘幅度 最常用 simple，12 个样本，一致性 92%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
