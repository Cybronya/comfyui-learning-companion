---
name: unknown_workflow_video_upscale_4
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9135
common_nodes: [LayerFilter: GaussianBlur, RH_DLSS5Enhance, VHS_LoadVideo, VHS_VideoCombine, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, 图像缩放V2_孤海]
problems: []
missing: []
members: [平台全量/VOSR2 + DLSS5 4K视频超分放大_2100967801958789121.json, 平台全量/VOSR2 + DLSS5 双重视频超分与画质增强_2104817431230377986.json, 平台全量/VOSR2 + DLSS5 视频超分放大_2100223278790037506.json, 平台全量/VOSR2 + DLSS5 视频超分放大_2101714086508716033.json, 平台全量/VOSR2 + DLSS5 视频超分放大_2102331588230078465.json, 平台全量/开源最强VOSR2 + DLSS5 视频超分放大（不改变原视频不用输入提示词）_2109591428304293889.json, 平台全量/视频增强丨VOSR2＋DLSS5丨超分放大_2120418933407834113.json, 视频生成/图生视频/VOSR2_+_DLSS5_视频超分放大_2115579106124451841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_4

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/VOSR2 + DLSS5 4K视频超分放大_2100967801958789121.json、平台全量/VOSR2 + DLSS5 双重视频超分与画质增强_2104817431230377986.json、平台全量/VOSR2 + DLSS5 视频超分放大_2100223278790037506.json、平台全量/VOSR2 + DLSS5 视频超分放大_2101714086508716033.json、平台全量/VOSR2 + DLSS5 视频超分放大_2102331588230078465.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `LayerFilter: GaussianBlur`
- `RH_DLSS5Enhance`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `GH_AudioVideoMerger` —— 7/8 个有
- `GH_ImageVideoComparer` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Int` —— 1/8 个有
- `SaveVideo` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
