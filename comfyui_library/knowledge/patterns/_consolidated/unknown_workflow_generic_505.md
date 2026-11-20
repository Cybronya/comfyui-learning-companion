---
name: unknown_workflow_generic_505
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.895833
common_nodes: [LoadAudio, LoadImage, LoadVideo, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/Seedance2.0 Fast全能参考视频_2040713981702180865.json, 视频生成/图生视频/Seedance2.0 fast 全能参考视频(支持真人)_2067073738482470914.json, 视频生成/文生视频/RhartVideoSparkvideo20FastMultimodalVideo+全节点注释_2052012439998345217.json, 视频生成/文生视频/RhartVideoSparkvideo20MultimodalVideo_2038486808283062273.json, 视频生成/文生视频/Seedance2.0全能参考视频（3张图片+1个参考视频+1条音频）支持真人_2101580146510749698.json, 视频生成/文生视频/视频生成seedance 2.0满血版_2058854158081552385.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_505

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Seedance2.0 Fast全能参考视频_2040713981702180865.json、视频生成/图生视频/Seedance2.0 fast 全能参考视频(支持真人)_2067073738482470914.json、视频生成/文生视频/RhartVideoSparkvideo20FastMultimodalVideo+全节点注释_2052012439998345217.json、视频生成/文生视频/RhartVideoSparkvideo20MultimodalVideo_2038486808283062273.json、视频生成/文生视频/Seedance2.0全能参考视频（3张图片+1个参考视频+1条音频）支持真人_2101580146510749698.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `RH_SparkVideoAssetCreate` —— 5/6 个有
- `RH_SparkVideoAssetIdsMerge` —— 5/6 个有
- `RH_RhartVideoSparkvideo20FastMultimodalVideo` —— 3/6 个有
- `RH_RhartVideoSparkvideo20MultimodalVideo` —— 3/6 个有
- `RH_SparkVideoAssetQuery` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `SoundFlow_TrimAudio` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
